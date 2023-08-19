from test.runTest import runTest
from test.mocks.BatteryInfoGetterMock import BatteryInfoGetterMockTests
from test.mocks.SpeakerMock import SpeakerMockTests
from test.mocks.TimeManagerMock import TimeManagerMockTests
from objects.BatteryMonitor import BatteryMonitorTests
from objects.BatteryInfoGetter import BatteryInfoGetterTests
from main import MainTest

TESTS_TO_RUN = [
    BatteryInfoGetterMockTests,
    SpeakerMockTests,
    TimeManagerMockTests,
    BatteryMonitorTests,
    BatteryInfoGetterTests,
    MainTest]

for test in TESTS_TO_RUN:
    print(f"STARTING - {test.__name__}")
    test()
