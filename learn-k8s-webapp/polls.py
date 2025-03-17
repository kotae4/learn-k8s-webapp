from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
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
    poll_api = votingApi.PollApi(votingApi.ApiClient(configuration=apiConfig))
    try:
        # Get list of all polls
        polls: list[votingApi.PollDetailsResponseModel] = poll_api.api_poll_get(offset=0, limit=10)
        voteSummaries: list[dict[str,int]] = []
        for poll in polls:
            try:
                pollDetails: votingApi.PollDetailsResponseModel = poll_api.api_poll_poll_id_get(poll_id=poll.poll_id)
                voteSummaries.append(pollDetails.vote_summary)
            except ApiException as e:
                flash(f"API error when fetching vote summary for poll '{poll.title}'")
                current_app.logger.error(f"Exception when calling poll->get_by_id: {e}")
    except ApiException as e:
        flash("API error when fetching all polls")
        current_app.logger.error(f"Exception when calling PollsApi->polls_get: {e}")
    current_app.logger.info(voteSummaries)
    return render_template('index.html', polls=polls, votes=voteSummaries)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        current_app.logger.info("Creating poll with following formdata:")
        current_app.logger.info(request.form)
        choices = request.form.getlist('choice[]')
        body = votingApi.CreatePollRequestModel(title=request.form['title'], 
                                        user=request.form['creator'],
                                        expiration=request.form['expiration'],
                                        short_description=request.form['shortDesc'],
                                        long_description=request.form['longDesc'],
                                        choices=choices)
        settings : Settings = get_settings()
        apiConfig: votingApi.Configuration = votingApi.Configuration()
        portPart = "" if settings.backend_port == 0 else (":" + str(settings.backend_port))
        apiConfig.host = settings.backend_protocol + "://" + settings.backend_host + portPart
        poll_api = votingApi.PollApi(votingApi.ApiClient(configuration=apiConfig))
        try:
            # post poll using form data
            current_app.logger.info("Creating poll with following body:")
            current_app.logger.info(body)
            api_response = poll_api.api_poll_post(body=body)
            current_app.logger.info(api_response)
            return redirect(url_for('polls.index'))
        except ApiException as e:
            flash("API error when creating poll")
            current_app.logger.exception(f"Exception when calling PollsApi->polls_post: {e}")
    return render_template('create.html')

@bp.route('/poll/<int:pollId>', methods=('GET', 'POST'))
def poll(pollId):
    settings : Settings = get_settings()
    apiConfig: votingApi.Configuration = votingApi.Configuration()
    portPart = "" if settings.backend_port == 0 else (":" + str(settings.backend_port))
    apiConfig.host = settings.backend_protocol + "://" + settings.backend_host + portPart
    poll_api = votingApi.PollApi(votingApi.ApiClient(configuration=apiConfig))
    pollInfo: votingApi.PollDetailsResponseModel = None
    if request.method == 'POST':
        vote_api = votingApi.VoteApi(votingApi.ApiClient(configuration=apiConfig))
        # cast the vote
        current_app.logger.info("Got request form:")
        current_app.logger.info(request.form)
        body = votingApi.CreateVoteRequestModel()
        body.poll_id = pollId
        body.choice_id = request.form['choice_id']
        body.user = "webuser"
        current_app.logger.info(f"Submitting vote with this body: {body}")
        try:
            voteInfo = vote_api.api_vote_post(body=body)
        except ApiException as e:
            flash("API error when voting")
            current_app.logger.exception(f"Exception when calling PollsApi->votes_poll_id_post: {e}")
    # get the poll details
    try:
        pollInfo = poll_api.api_poll_poll_id_get(poll_id=pollId)
    except ApiException as e:
        flash("API error when getting detailed poll info")
        current_app.logger.exception(f"Exception when calling PollsApi->polls_poll_id_get: {e}")
    return render_template('poll.html', poll=pollInfo)