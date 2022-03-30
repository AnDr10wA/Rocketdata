from rest_framework import serializers
from .models import ReposInfo


class ProjectListSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReposInfo
        fields = ('default_link',)


class ReposListSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReposInfo
        fields = ('name_repo',)


class StatsSerializers(serializers.Serializer):

    users = serializers.CharField(max_length=50)
    repos = serializers.CharField(max_length=50)
    average_repos = serializers.CharField(max_length=50)

class StatsOneSerializers(serializers.Serializer):
    repo_max_commit = serializers.CharField(max_length=50)
    repo_name = serializers.CharField(max_length=50)
    av_stars = serializers.CharField(max_length=50)