from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import os

def user_directory_path(instance, filename):
    """ Save file as 'videos/{username}.{ext}' """
    ext = filename.split('.')[-1]  # Get file extension
    filename = f"{instance.user.username}.{ext}"  # Fixed filename per user
    return os.path.join('videos/', filename)

class VideoUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # One user can have multiple videos
    video = models.FileField(upload_to=user_directory_path)
    processed_result = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.uploaded_at}"

    def save(self, *args, **kwargs):
        """ Ensure only one video per user by deleting the previous one before saving the new one """
        old_videos = VideoUpload.objects.filter(user=self.user)
        for old_video in old_videos:
            if old_video.video and old_video.video.name != self.video.name:
                try:
                    # Close the file if it's open
                    if hasattr(old_video.video, 'close'):
                        old_video.video.close()
                    # Try deleting the file
                    old_video.video.delete(save=False)
                except Exception as e:
                    print(f"[WARNING] Could not delete video file: {e}")
            try:
                old_video.delete()
            except Exception as e:
                print(f"[WARNING] Could not delete old DB record: {e}")

        super().save(*args, **kwargs)
