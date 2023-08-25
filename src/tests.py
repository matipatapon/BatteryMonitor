import sys
from test.runTest import runTest
from test.mocks.BatteryInfoGetterMock import BatteryInfoGetterMockUTs
from test.mocks.SpeakerMock import SpeakerMockUTs
from test.mocks.TimeManagerMock import TimeManagerMockUTs
from objects.BatteryMonitor import BatteryMonitorUTs
from objects.BatteryInfoGetter import BatteryInfoGetterITs
from main import MainITs

UT_TO_RUN = [
    BatteryInfoGetterMockUTs,
    SpeakerMockUTs,
    TimeManagerMockUTs,
    BatteryMonitorUTs
]

IT_TO_RUN = [
    MainITs,
    BatteryInfoGetterITs
]

def runTests(tests):
    for test in tests:
        print(f"STARTING - {test.__name__}")
        test()


if "ut" in sys.argv:
    runTests(UT_TO_RUN)

if "it" in sys.argv:
    runTests(IT_TO_RUN)
