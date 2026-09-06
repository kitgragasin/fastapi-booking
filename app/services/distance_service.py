from math import asin, cos, radians, sin, sqrt


class DistanceService:
    EARTH_RADIUS_KM = 6371.0

    def haversine_km(
        self,
        latitude_1: float,
        longitude_1: float,
        latitude_2: float,
        longitude_2: float,
    ) -> float:
        lat1 = radians(latitude_1)
        lon1 = radians(longitude_1)
        lat2 = radians(latitude_2)
        lon2 = radians(longitude_2)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        arc = (
            sin(delta_lat / 2) ** 2
            + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
        )
        central_angle = 2 * asin(sqrt(arc))
        return self.EARTH_RADIUS_KM * central_angle
