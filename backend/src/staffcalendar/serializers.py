from rest_framework import serializers

from users.models import Batch
from .models import MonthlyRoster


class RosterSerializer(serializers.ModelSerializer):
	work_day = serializers.CharField(source='work_day.day_symbol')
	shift = serializers.CharField(source='shift.name')
	batch = serializers.CharField(source='batch.name')

	class Meta:
		model = MonthlyRoster
		fields = ["id","week_start_date", "shift_date", "work_day","shift", "batch"]

class RosterCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = MonthlyRoster
		fields = "__all__"

class RosterUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = MonthlyRoster
		fields = "__all__"


class BatchSerializer(serializers.ModelSerializer):
	rosters = RosterSerializer(many=True, read_only=True)

	class Meta:
		model = Batch
		fields = ["id", "name", "rosters"]

class BatchCreateSerializer(serializers.ModelSerializer):
	rosters = RosterSerializer(many=True, read_only=True)

	class Meta:
		model = Batch
		fields = ["id", "name", "rosters"]