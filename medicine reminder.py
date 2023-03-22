import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Please Take a Dolo 650Mg Medicine!",
        message="As per your medical prescription",
        app_icon="C:\Users\saiga\PycharmProjects\KratinProject\Pictogrammers-Material-Medication.ico",
        timeout=5
    )
    time.sleep(60 * 60)
