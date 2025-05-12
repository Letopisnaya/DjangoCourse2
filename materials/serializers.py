from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidators


class CourseSerializer(ModelSerializer):
    is_subscribed = SerializerMethodField()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):

    class Meta:
        validators = [LinkValidators(field="video")]
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lessons_in_course = SerializerMethodField()
    lessons_list = LessonSerializer(many=True, read_only=True, source="lesson_set")

    def get_count_lessons_in_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lessons_in_course",
            "lessons_list",
        )


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
