from typing import TypedDict, Optional, Dict

# This defines the data our agents will pass to each other
class ReviewState(TypedDict):
    username: str
    github_data: Optional[Dict]
    feedback: Optional[str]