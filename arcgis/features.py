from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import requests

from arcgis.auth import Auth


@dataclass
class FeatureLayer:
    url: str
    auth: Auth = field(repr=False)
    token: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.token = self.auth.get_token()

    def query(
        self,
        where: str = "1=1",
        out_fields: List[str] = ["*"],
        return_geometry: bool = True,
        order_by_fields: Optional[str] = None,
        result_record_count: Optional[int] = None,
    ) -> Dict[str, Any]:
        params = {
            "where": where,
            "outFields": ",".join(out_fields),
            "returnGeometry": return_geometry,
            "orderByFields": order_by_fields,
            "resultRecordCount": result_record_count,
            "token": self.token,
            "f": "json",
        }
        response = requests.get(f"{self.url}/query", params=params)
        return response.json()


@dataclass
class FeatureSet:
    pass
