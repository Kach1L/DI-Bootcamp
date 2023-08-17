from django.urls import path
from .views import Rental,Customer,CustomerAdd,VehicleDetail,VehicleAdd,RentalStationList,RentalStationAdd,RentalStationDetail,VehicleDistribution,DistributeVehicles,MonthlyRentalStats,PopularRentalStation,PopularVehicleType

urlpatterns = [
    # XP Paths
    path('/rent/rental/', Rental.as_view(), name='rental'),
    path('/rent/rental/<pk>', Rental.as_view(), name='specific-rental'),
    path('/rent/customer/', Customer.as_view(), name='customer'),
    path('/rent/customer/add', CustomerAdd.as_view(), name='customer-add'),
    path('/rent/vehicle/', Rental.as_view(), name='rental-type'),
    path('/rent/vehicle/<pk>', VehicleDetail.as_view(), name='vehicle-detail'),
    path('/rent/vehicle/add', VehicleAdd.as_view(), name='vehicle-add'),
    path('/rent/station', RentalStationList.as_view(), name='rental-station-list'),
    path('/rent/station/add', RentalStationAdd.as_view(), name='rental-station-add'),
    path('/rent/station/<station_id>', RentalStationDetail.as_view(), name='rental-station-detail'),
    path('/rent/station/distribution', VehicleDistribution.as_view(), name='vehicle-distribution'),
    path('/rent/station/distribute', DistributeVehicles.as_view(), name='distribute-vehicles'),
    path('/rent/vehicle/<pk>', VehicleDetail.as_view(), name='vehicle-detail'),
    
    # Daily Ch Paths
    path('stats/monthly/', MonthlyRentalStats.as_view(), name='monthly-rental-stats'),
    path('stats/popular_station/', PopularRentalStation.as_view(), name='popular-station-stats'),
    path('stats/popular_vehicle_type/', PopularVehicleType.as_view(), name='popular-vehicle-type-stats'),
]
