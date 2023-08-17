from rest_framework import serializers
from .models import Customer,Vehicle,VehicleType,VehicleSize,Rental,RentalRate,RentalStation,Address,VehicleAtRentalStation

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customer-detail')  # Adjust the view name

    class Meta:
        model = Customer
        fields = ['url', 'id', "first_name", "last_name", "email", "phone_number", "address"]
        
class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicle-detail')  # Adjust the view name

    class Meta:
        model = Vehicle
        fields = ['url', 'id', "vehicle_type", "date_created", "real_cost", "size"]
        
class VehicleDetailSerializer(serializers.ModelSerializer):
    current_station = serializers.SerializerMethodField()
    last_rental = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = '__all__'

    def get_current_station(self, obj):
        try:
            current_station = VehicleAtRentalStation.objects.filter(vehicle=obj, departure_date__isnull=True).last()
            return {
                'station_id': current_station.station.id,
                'station_name': current_station.station.name
            }
        except VehicleAtRentalStation.DoesNotExist:
            return None

    def get_last_rental(self, obj):
        try:
            last_rental = obj.rentals.order_by('-rental_date').first()
            if last_rental:
                return {
                    'customer': f"{last_rental.customer.first_name} {last_rental.customer.last_name}",
                    'station': last_rental.rental_station.name
                }
        except:
            return None
    
class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicle_type-detail')  # Adjust the view name

    class Meta:
        model = VehicleType
        fields = ['url', 'id', "name"]
    
class VehicleSizeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicle_size-detail')  # Adjust the view name

    class Meta:
        model = VehicleSize
        fields = ['url', 'id', "name"]
        

class RentalSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rental-detail')  # Adjust the view name

    class Meta:
        model = Rental
        fields = ['url', 'id', "rental_date", "return_date", "customer", "vehicle"]
        

class RentalRateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rental_rate-detail')  # Adjust the view name

    class Meta:
        model = RentalRate
        fields = ['url', 'id', "daily_rate", "vehicle_type", "vehicle_size"]
        

class RentalStationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='rentalstation-detail')  # Adjust the view name

    class Meta:
        model = RentalStation
        fields = ['url', 'id', "name", "capacity", "address"]
        

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='address-detail')  # Adjust the view name

    class Meta:
        model = Address
        fields = ['url', 'id', "address", "address2", "city", "country", "postal_code"]
        
    
class VehicleAtRentalStationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='vehicleatrentalstation-detail')  # Adjust the view name

    class Meta:
        model = VehicleAtRentalStation
        fields = ['url', 'id', "arrival_date", "departure_date", "vehicle"]