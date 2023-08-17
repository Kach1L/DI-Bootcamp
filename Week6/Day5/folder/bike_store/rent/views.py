from django.shortcuts import render
from .serializers import CustomerSerializer,VehicleSerializer,VehicleTypeSerializer,VehicleSizeSerializer,RentalSerializer,RentalRateSerializer,RentalStationSerializer,AddressSerializer,VehicleAtRentalStationSerializer,VehicleDetailSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Customer,Vehicle,VehicleType,VehicleSize,Rental,RentalRate,RentalStation,Address,VehicleAtRentalStation
from rest_framework import status
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# from .permissions import IsDepartmentAdmin, Is

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RentalsAPIView(APIView):
    
    # permission_classes = [IsDepartmentAdmin]
    
    def get(self, request, format=None):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(data=serializer.data)
    
    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class RentalsAPIView(APIView):
    
    # permission_classes = [IsDepartmentAdmin]
    
    def get(self, request,pk, format=None):
        rentals = Rental.objects.get(id=pk)
        serializer = RentalSerializer(rentals, many=True)
        return Response(data=serializer.data)

    def put(self, request, pk, format=None):
        rentals = Rental.objects.get(id=pk)
        serializer = RentalSerializer(instance=rentals, data=request.data)
    
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rentals = Rental.objects.get(id=pk)
        
        self.check_object_permissions(request, rentals)
        
        rentals.delete()
        return Response({'message':f'Rental id - {pk} DELETED'})
    

class CustomerList(APIView):

    def get(self, request, format=None):
        customers = Customer.objects.all().order_by('last_name', 'first_name')
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerAdd(APIView):

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleTypeList(APIView):

    def get(self, request, format=None):
        vehicle_types = VehicleType.objects.all()
        serializer = VehicleTypeSerializer(vehicle_types, many=True)
        return Response(serializer.data)

class VehicleDetail(APIView):

    def get(self, request, pk, format=None):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VehicleAdd(APIView):

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RentalStationList(APIView):

    def get(self, request, format=None):
        rental_stations = RentalStation.objects.all()
        serializer = RentalStationSerializer(rental_stations, many=True)
        return Response(serializer.data)  


class RentalStationAdd(APIView):

    def post(self, request, format=None):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RentalStationDetail(APIView):

    def get(self, request, station_id, format=None):
        try:
            station = RentalStation.objects.get(pk=station_id)
        except RentalStation.DoesNotExist:
            return Response({"error": "Rental station not found"}, status=status.HTTP_404_NOT_FOUND)
        
        vehicles_at_station = VehicleAtRentalStation.objects.filter(station=station)
        serializer = VehicleAtRentalStationSerializer(vehicles_at_station, many=True)
        
        station_data = RentalStationSerializer(station).data
        station_data["vehicles_at_station"] = serializer.data

        return Response(station_data)
    
    
class VehicleDistribution(APIView):

    def get(self, request, format=None):
        stations = RentalStation.objects.all()
        distribution_data = []

        for station in stations:
            vehicles_at_station = VehicleAtRentalStation.objects.filter(station=station)
            serializer = VehicleAtRentalStationSerializer(vehicles_at_station, many=True)
            
            station_data = {
                "station_id": station.id,
                "station_name": station.name,
                "vehicle_count": len(vehicles_at_station),
                "vehicles": serializer.data
            }
            distribution_data.append(station_data)

        return Response(distribution_data)


class DistributeVehicles(APIView):

    def post(self, request, format=None):
        # Calculate the desired number of vehicles per station based on total vehicles and stations
        total_vehicles = Vehicle.objects.count()
        total_stations = RentalStation.objects.count()
        vehicles_per_station = total_vehicles // total_stations

        # Get the list of stations and their current vehicle count
        stations = RentalStation.objects.annotate(current_vehicles=Count('vehicles'))

        # Distribute vehicles evenly among stations
        for station in stations:
            vehicles_to_add = vehicles_per_station - station.current_vehicles
            if vehicles_to_add > 0:
                available_vehicles = Vehicle.objects.filter(vehicleatrentalstation__departure_date__isnull=True)
                vehicles_to_move = available_vehicles[:vehicles_to_add]
                for vehicle in vehicles_to_move:
                    VehicleAtRentalStation.objects.create(station=station, vehicle=vehicle)

        return Response({"message": "Vehicles distributed among stations."}, status=status.HTTP_200_OK)
    
class VehicleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDetailSerializer
    
class MonthlyRentalStats(APIView):

    def get(self, request, format=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        queryset = Rental.objects.all()

        if start_date and end_date:
            queryset = queryset.filter(rental_date__range=(start_date, end_date))

        monthly_stats = queryset.annotate(month=TruncMonth('rental_date')) \
            .values('month') \
            .annotate(rentals=Count('id')) \
            .order_by('month')
        
        result = {stat['month'].strftime('%Y-%m'): stat['rentals'] for stat in monthly_stats}
        
        return Response(result)

    
class PopularRentalStation(APIView):

    def get(self, request, format=None):
        popular_stations = RentalStation.objects.annotate(total_rentals=Count('rentals')) \
            .values('name', 'total_rentals') \
            .order_by('-total_rentals')
        
        result = {station['name']: station['total_rentals'] for station in popular_stations}
        
        return Response(result)

class PopularVehicleType(APIView):

    def get(self, request, format=None):
        popular_vehicle_types = Rental.objects.values('vehicle__vehicle_type__name') \
            .annotate(total_rentals=Count('id')) \
            .order_by('-total_rentals')
        
        result = {vehicle_type['vehicle__vehicle_type__name']: vehicle_type['total_rentals'] for vehicle_type in popular_vehicle_types}
        
        return Response(result)
    
     
    # def put(self, request, pk, *args, **kwargs):
    #     departments = Department.objects.get(id=pk)
    #     serializer = DepartmentSerializer(instance=departments, data=request.data)
    
    #     if serializer.valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def delete(self, request, pk, *args, **kwargs):
    #     departments = Department.objects.get(id=pk)
        
    # self.check_object_permissions(request, departments)
        
    # departments.delete()
    # return Response({'message':f'Department id - {pk} DELETED'})