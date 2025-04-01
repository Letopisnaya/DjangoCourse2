from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
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