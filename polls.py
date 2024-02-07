from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from . import votingApi
from .votingApi.rest import ApiException
from .config import Settings, get_settings

bp = Blueprint('polls', __name__)

@bp.route('/')
def index():
    settings : Settings = get_settings()
    apiConfig: votingApi.Configuration = votingApi.Configuration()
    portPart = "" if settings.backend_port == 0 else (":" + str(settings.backend_port))
    apiConfig.host = settings.backend_protocol + "://" + settings.backend_host + portPart
    api_instance = votingApi.DefaultApi(votingApi.ApiClient(configuration=apiConfig))
    try:
        # Get list of all polls
        polls: list[votingApi.PollRead] = api_instance.get_polls_polls_get()
        voteSummaries: list[votingApi.VoteSummary] = []
        for poll in polls:
            try:
                voteInfo = api_instance.get_votes_votes_poll_id_get(poll.poll_id)
                voteSummaries.append(voteInfo)
            except ApiException as e:
                flash(f"API error when fetching vote summary for poll '{poll.title}'")
                print(f"Exception when calling poll->get_vote_summary: {e}")
    except ApiException as e:
        flash("API error when fetching all polls")
        print(f"Exception when calling PollsApi->polls_get: {e}")
    print(voteSummaries)
    return render_template('index.html', polls=polls, votes=voteSummaries)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        print("Creating poll with following formdata:")
        print(request.form)
        choices = request.form.getlist('choice[]')
        body = votingApi.PollCreate(title=request.form['title'], 
                                        creator_id=request.form['creator'],
                                        expiration_time=request.form['expiration'],
                                        short_description=request.form['shortDesc'],
                                        long_description=request.form['longDesc'],
                                        choices=choices)
        settings : Settings = get_settings()
        apiConfig: votingApi.Configuration = votingApi.Configuration()
        portPart = "" if settings.backend_port == 0 else (":" + str(settings.backend_port))
        apiConfig.host = settings.backend_protocol + "://" + settings.backend_host + portPart
        api_instance = votingApi.DefaultApi(votingApi.ApiClient(configuration=apiConfig))
        try:
            # post poll using form data
            print("Creating poll with following body:")
            print(body)
            api_response = api_instance.create_poll_polls_post(body=body)
            print(api_response)
            return redirect(url_for('polls.index'))
        except ApiException as e:
            flash("API error when creating poll")
            print(f"Exception when calling PollsApi->polls_post: {e}")
    return render_template('create.html')

@bp.route('/poll/<int:pollId>', methods=('GET', 'POST'))
def poll(pollId):
    settings : Settings = get_settings()
    apiConfig: votingApi.Configuration = votingApi.Configuration()
    portPart = "" if settings.backend_port == 0 else (":" + str(settings.backend_port))
    apiConfig.host = settings.backend_protocol + "://" + settings.backend_host + portPart
    api_instance = votingApi.DefaultApi(votingApi.ApiClient(configuration=apiConfig))
    pollInfo = None
    voteInfo: votingApi.VoteSummary = None
    if request.method == 'POST':
        # cast the vote
        print("Got request form:")
        print(request.form)
        body = votingApi.VoteBase()
        body.poll_id = pollId
        body.choice_id = request.form['choice_id']
        body.user_id = "webuser"
        try:
            voteInfo = api_instance.create_vote_votes_poll_id_post(poll_id=pollId, body=body)
        except ApiException as e:
            flash("API error when voting")
            print(f"Exception when calling PollsApi->votes_poll_id_post: {e}")
    else:
        try:
            voteInfo = api_instance.get_votes_votes_poll_id_get(pollId)
            print("Got voteInfo!")
        except ApiException as e:
            flash("API error when getting votes")
            print(f"Exception when calling PollsApi->votes_poll_id_get: {e}")
    # get the poll details
    try:
        pollInfo = api_instance.get_poll_polls_poll_id_get(pollId)
    except ApiException as e:
        flash("API error when getting detailed poll info")
        print(f"Exception when calling PollsApi->polls_poll_id_get: {e}")
    print(voteInfo)
    return render_template('poll.html', poll=pollInfo, votes=voteInfo)