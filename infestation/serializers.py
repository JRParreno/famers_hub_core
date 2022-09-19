from pyexpat import model
from rest_framework import serializers
from .models import Infestation, Symptom, PreventMeasure
from insect.serializers import InsectSerializer
from chemical_control.serializers import ChemicalControlSerializer


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = '__all__'


class PreventMeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreventMeasure
        fields = '__all__'


class InfestationSerializer(serializers.ModelSerializer):
    insect = InsectSerializer()

    class Meta:
        model = Infestation
        fields = ['pk', 'insect', 'recommendation_description',
                  'organic_control', 'link']

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(InfestationSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super(InfestationSerializer,
                     self).to_representation(instance)

        if 'request' in self.context and self.request:

            symptoms = SymptomSerializer(
                instance.infestaion_symptom.all(), many=True, context={"request": self.request})
            prevent_measures = PreventMeasureSerializer(
                instance.infestaion_prevent_measure.all(), many=True, context={"request": self.request})
            chemical_controls = ChemicalControlSerializer(
                instance.chemical_control_infestation.all(), many=True, context={"request": self.request})

            data['symptoms'] = symptoms.data
            data['prevent_measures'] = prevent_measures.data
            data['chemical_controls'] = chemical_controls.data
        return data
