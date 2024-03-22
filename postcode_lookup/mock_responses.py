from response_builder.v1.generated_responses.root_responses import (
    CANCELLED_BALLOT_CANDIDATE_DEATH,
    CANCELLED_BALLOT_EQUAL_CANDIDATES,
    CANCELLED_BALLOT_NO_CANDIDATES,
    CANCELLED_BALLOT_UNDER_CONTESTED,
    MULTIPLE_BALLOTS_WITH_CANCELLATION,
    MULTIPLE_BALLOTS_WITH_VOTING_SYSTEM_AND_POLLING_STATION,
    NO_LOCAL_BALLOTS,
    ONE_CANCELLED_BALLOT_ONE_NOT,
    SINGLE_LOCAL_FUTURE_BALLOT_WITH_POLLING_STATION,
    SINGLE_LOCAL_FUTURE_BALLOT_WITHOUT_POLLING_STATION,
)

__ALL__ = ("example_responses",)
example_responses = {
    "AA1 1AA": {
        "description": "No local ballots",
        "response": NO_LOCAL_BALLOTS,
    },
    "CA1 1AB": {
        "description": "Cancelled ballot due to candidate death",
        "response": CANCELLED_BALLOT_CANDIDATE_DEATH,
    },
    "CA1 2AB": {
        "description": "Cancelled ballot due to no candidates",
        "response": CANCELLED_BALLOT_NO_CANDIDATES,
    },
    "CA1 3AB": {
        "description": "Cancelled ballot due to equal number of candidates",
        "response": CANCELLED_BALLOT_EQUAL_CANDIDATES,
    },
    "CA1 4AB": {
        "description": "Cancelled ballot due to not enough candidates",
        "response": CANCELLED_BALLOT_UNDER_CONTESTED,
    },
    "CA1 5AB": {
        "description": "One cancelled ballot, one not cancelled",
        "response": ONE_CANCELLED_BALLOT_ONE_NOT,
    },
    "AA1 1AC": {
        "description": "Single local ballot (One upcoming ballot, station known, with candidates)",
        "response": SINGLE_LOCAL_FUTURE_BALLOT_WITH_POLLING_STATION,
    },
    "AA1 1AD": {
        "description": "Single local ballot (One upcoming ballot, station not known, with candidates)",
        "response": SINGLE_LOCAL_FUTURE_BALLOT_WITHOUT_POLLING_STATION,
    },
    "AA1 1AF": {
        "description": "Multiple ballots including Greater London Assembly and Mayoral with voting system and polling station",
        "response": MULTIPLE_BALLOTS_WITH_VOTING_SYSTEM_AND_POLLING_STATION,
    },
    "AA1 1AG": {
        "description": "Multiple ballots including a Local, GLA, Mayoral, Parliamentary ballots including one cancellation.",
        "response": MULTIPLE_BALLOTS_WITH_CANCELLATION,
    },
    # "AA1 1AH": {
    #     "description": "Parliamentary ballot",
    #     "response": PARL_BALLOT,
    # },
    # "AA1 1AI": {
    #     "description": "London Assembly ballot",
    #     "response": GLA_BALLOT,
    # },
    # "AA1 1AJ": {
    #     "description": "Mayoral ballot",
    #     "response": MAYORAL_BALLOT,
    # },
    # "AA1 1AK": {
    #     "description": "Police and Crime Commissioner ballot",
    #     "response": PCC_BALLOT,
    # },
}
