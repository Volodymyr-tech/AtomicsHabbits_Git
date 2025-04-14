from rest_framework import serializers

from atomicshabbits.models import Habbits
from atomicshabbits.validators import (
    ConnectedHabitOrRewardValidator,
    FrequencyOfHabitValidator,
    PositiveHabitOnlyValidator,
    RelatedHabitValidator,
)

# from atomicshabbits.validators import TimeValidator


class HabbitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habbits
        fields = "__all__"
        validators = [
            ConnectedHabitOrRewardValidator("connected_habbit", "award"),
            RelatedHabitValidator("connected_habbit"),
            PositiveHabitOnlyValidator(
                "is_pleasant_habit", "award", "connected_habbit"
            ),
            FrequencyOfHabitValidator("periodicity"),
        ]

    def validate_time_to_do(self, value):
        if 0 < value <= 120:
            return value
        else:
            raise serializers.ValidationError(
                "Time to do should be from 0-120 seconds"
            )
