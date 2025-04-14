from rest_framework import serializers


class BaseValidator:
    def __init__(self, *args):
        """When creating a validator object,
        we can pass any number of fields
        (field name, as a string)"""
        self.fields = args

    def __call__(self, value):
        print(f" here are {self.fields}")
        field_values = {
            field: value.get(field) for field in self.fields
        }  # getting the dict of values from serializer, can be string,int, objects etc.
        print(field_values)
        self.validate(
            **field_values
        )  # pass dict with values to validation func

    def validate(self, **kwargs):
        """Abstract method"""
        raise NotImplementedError(
            "You should realize that method in your validation classes"
        )


class ConnectedHabitOrRewardValidator(BaseValidator):
    """
    Checks that the associated habit and reward are not specified at the same time.
    """

    def validate(self, connected_habbit, award, **kwargs):
        if connected_habbit and award:
            raise serializers.ValidationError(
                "Simultaneous selection of a related habit"
                " and remuneration is prohibited"
            )


class RelatedHabitValidator(BaseValidator):
    """
    Verifies that the associated habit is pleasant
    """

    def validate(self, connected_habbit, **kwargs):
        if connected_habbit and not connected_habbit.is_pleasant_habit:
            raise serializers.ValidationError(
                "A related habit should be pleasant."
            )


class PositiveHabitOnlyValidator(BaseValidator):
    """
    Checks that a pleasant habit has no reward.
    or a related habit
    """

    def validate(self, is_pleasant_habit, award, connected_habbit, **kwargs):
        if is_pleasant_habit and (award or connected_habbit):
            raise serializers.ValidationError(
                "There can be no reward for a pleasant habit."
                "or a related habit"
            )


class FrequencyOfHabitValidator(BaseValidator):
    """
    Checks that the habit is performed at least once every 7 days.
    """

    def validate(self, periodicity, **kwargs):
        if periodicity is not None and not (1 <= periodicity <= 7):
            raise serializers.ValidationError(
                "You should not perform the habit less than once every 7 days."
            )
