from rest_framework import serializers
from .models import ChemicalControl, ChemicalInsecticide, ChemicalInstruction, ChemicalSafetyPrecaution
from insecticide.serializers import InsecticideSerializer


class ChemicalInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalInstruction
        fields = ['pk', 'description', 'icon_image', 'link', ]


class ChemicalSafetyPrecautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalSafetyPrecaution
        fields = ['pk', 'description', 'icon_image', 'link', 'hazard_level']


class ChemicalInsecticideSerializer(serializers.ModelSerializer):
    insecticide = InsecticideSerializer()

    class Meta:
        model = ChemicalInsecticide
        fields = ['pk', 'insecticide', 'percentage']


class ChemicalControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalControl
        fields = ['pk', 'reminder', 'link']

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(ChemicalControlSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super(ChemicalControlSerializer,
                     self).to_representation(instance)

        if 'request' in self.context and self.request:

            instructions = ChemicalInstructionSerializer(
                instance.chemical_control_instruction.all(), many=True, context={"request": self.request})
            safety_precautions = ChemicalSafetyPrecautionSerializer(
                instance.chemical_control_precaution.all(), many=True, context={"request": self.request})
            insecticides = ChemicalInsecticideSerializer(
                instance.chemical_control_insecticide.all(), many=True, context={"request": self.request})

            data['instructions'] = instructions.data
            data['safety_precautions'] = safety_precautions.data
            data['insecticides'] = insecticides.data
        return data
