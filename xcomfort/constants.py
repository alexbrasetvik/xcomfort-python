from enum import IntEnum


class Messages(IntEnum):
    NACK = 0
    ACK = 1
    HEARTBEAT = 2
    CONNECTION_START = 10
    CONNECTION_CONFIRM = 11
    CONNECTION_ESTABLISHED = 12
    CONNECTION_DECLINED = 13
    SC_INIT = 14
    SC_PUBKEY = 15
    SC_SECRET = 16
    SC_ESTABLISHED = 17
    SC_INVALID = 18
    AUTH_LOGIN = 30
    AUTH_LOGIN_DENIED = 31
    AUTH_LOGIN_SUCCESS = 32
    AUTH_APPLY_TOKEN = 33
    AUTH_APPLY_TOKEN_RESPONSE = 34
    AUTH_VERIFY_TOKEN = 35
    AUTH_VERIFY_TOKEN_RESPONSE = 36
    AUTH_RENEW_TOKEN = 37
    AUTH_RENEW_TOKEN_RESPONSE = 38
    AUTH_KILL_TOKEN = 39
    TEST_ON = 100
    TEST_OFF = 101
    TEST_CRYPTO = 102
    TEST_ALERT = 104
    TEST_DEVICE_STATE = 105
    TEST_COMMAND = 120
    INITIAL_DATA = 240
    HOME_DATA = 242
    DIAGNOSTICS = 243
    INIT_SWUPDATE = 247
    DATA_SWUPDATE = 248
    START_SWUPDATE = 249
    UPDATE_BRIDGE = 250
    START_LEARNMODE = 251
    STOP_LEARNMODE = 252
    BARCODE_DEVICE = 253
    UPDATE_DEVICE = 254
    DELETE_DEVICE = 255
    ARRANGE_DEVICES = 256
    SET_ROOM = 257
    DELETE_ROOM = 259
    ARRANGE_ROOMS = 260
    SET_SCENE = 261
    DELETE_SCENE = 263
    ARRANGE_SCENES = 264
    EDIT_RF_PWD = 270
    SET_TIME = 271
    SET_ASTRO = 272
    SET_TIMER = 273
    DELETE_TIMER = 274
    ACTION_SLIDE_DEVICE = 280
    ACTION_SWITCH_DEVICE = 281
    ACTION_SLIDE_ROOM = 283
    ACTION_SWITCH_ROOM = 284
    ACTIVATE_SCENE = 285
    ADD_DEVICE = 290
    SET_DEVICE_STATE = 291
    SET_DEVICE_INFO = 292
    SET_ROOM_STATE = 293
    SET_ROOM_INFO = 294
    APP_INFO = 295
    DEVICE_DELETED = 296
    ROOM_DELETED = 297
    SCENE_DELETED = 298
    SET_ALL_DATA = 300
    SET_ROOM_ID = 301
    SET_SCENE_ID = 302
    SET_HOME_DATA = 303
    SET_DIAGNOSTICS = 304
    SET_TIMER_ID = 305
    FOUND_COMP = 306
    ADD_COMP = 307
    SET_COMP_INFO = 308
    COMP_DELETED = 309
    SET_STATE_INFO = 310
    CONFIG_SAVED = 311
    CONFIG_LIST = 312
    RESTORE_CONFIG_RESPONSE = 313
    SET_HEATING_PROGRAM = 350
    DELETE_HEATING_PROGRAM = 351
    SET_ROOM_HEATING = 352
    SET_HEATING_STATE = 353
    SET_ROOM_SHADING_STATE = 354
    SET_DEVICE_SHADING_STATE = 355
    SET_DEVICE_ALARM_STATE = 356
    GET_INTEGRATION = 357
    UNLINK_INTEGRATION = 358
    SET_HEATING_PROGRAM_ID = 360
    HEATING_PROGRAM_DELETED = 362
    SET_ROOM_HEATING_STATE = 363
    SET_BRIDGE_STATE = 364
    IDLE = -1
    NACK_INFO_INVALID_ACTION = -98
    NACK_INFO_DEVICE_NOT_DIMMABLE = -99
    NACK_INFO_UNKNOWN_DEVICE = -100


class ShadeOperationState(IntEnum):
    OPEN = 0
    CLOSE = 1
    STOP = 2
    STEP_DOWN = 3
    STEP_UP = 4
    GO_TO = 5
    CALIBRATION = 10
    LOCK = 11
    UNLOCK = 12
    QUIT = 13


class DeviceTypes(IntEnum):
    ACTUATOR_SWITCH = 100
    ACTUATOR_DIMM = 101
    SHADING_ACTUATOR = 102
    SWITCH = 202
    ROCKER = 220
    TEMP_SENSOR = 410
    HEATING_ACTUATOR = 440
    HEATING_VALVE = 441
    HEATING_WATER_VALVE = 442
    RC_TOUCH = 450
    TEMP_HUMIDITY_SENSOR = 451
    WATER_GUARD = 497
    WATER_SENSOR = 499


class HeatingTypes(IntEnum):
    ELECTRIC_FLOOR_FOIL = 1
    ELECTRIC_FLOOR_CABLE = 2
    WATER_FLOOR = 3
    ELECTRIC_RADIATOR = 4
    ELECTRIC_INFRARED = 5
    WATER_RADIATOR = 6


class ComponentTypes(IntEnum):
    PUSH_BUTTON_1 = 1
    PUSH_BUTTON_2 = 2
    MULTI_HEATING_ACTUATOR = 71
    LIGHT_SWITCH_ACTUATOR = 74
    DOOR_WINDOW_SENSOR = 76
    DIMMING_ACTUATOR = 77
    RC_TOUCH = 78
    BRIDGE = 83
    WATER_GUARD = 84
    WATER_SENSOR = 85
    SHADING_ACTUATOR = 86
