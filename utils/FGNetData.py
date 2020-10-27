FG_NET_FDM_VERSION = 24  # udp版本？
FG_MAX_ENGINES = 4  # 最大引擎数量 枚举数字为0
FG_MAX_WHEELS = 3  # 最大滑轮数 枚举数字为1
FG_MAX_TANKS = 4  # 最大油箱数量 枚举数字为2


class FGNetData:
    """网络数据与主机数据转换工具"""

    def __init__(self):
        """初始化方法，将所有数据结构中的数据都初始化一次，大部分为零"""

        version = 0  # 当数据值改变时增加
        padding = 0  # 填补？

        # Positions
        longitude = 0  # geodetic(radians)
        latitude = 0  # geodetic(radians)
        altitude = 0  # above sea level (meters)
        agl = 0  # above above ground level (meters)
        phi = 0  # roll(radians)
        theta = 0  # pitch(radians)
        psi = 0  # yaw or true heading(radians)
        alpha = 0  # angle of attack(radians)
        beta = 0  # side slip angle(radians)

       # Velocities

        phidot = 0  # roll  rate(radians / sec)
        thetadot = 0  # pitch rate(radians / sec)
        psidot = 0  # yaw  rate(radians / sec)
        vcas = 0  # calibrated airspeed
        climb_rate = 0  # feet per second
        v_north = 0  # north velocity in local / body frame, fps
        v_east = 0  # east velocity in local / body frame, fps
        v_down = 0  # down / vertical velocity in local / body  frame, fps
        v_wind_body_north = 0  # north velocity in local / body frame

        # relative to local airmass, fps

        v_wind_body_east = 0  # east velocity in local / body frame

        # relative to local airmass, fps

        v_wind_body_down = 0  # down / vertical velocity in local / body

        # frame relative to local airmass, fps

        # Accelerations

        A_X_pilot = 0  # X accel in body frame ft / sec ^ 2
        A_Y_pilot = 0  # Y accel in body frame ft / sec ^ 2
        A_Z_pilot = 0  # Z accel in body frame ft / sec ^ 2

        # Stall

        stall_warning = 0  # 0.0 - 1.0 indicating the amount of stall
        slip_deg = 0  # slip ball deflection

        # Pressure

        # Engine status

        num_engines = 0  # Number of valid engines

        eng_state = [0] * FG_MAX_ENGINES  # Engine state(off, cranking, running)
        rpm = [0] * FG_MAX_ENGINES  # Engine RPM rev / min
        fuel_flow = [0] * FG_MAX_ENGINES  # Fuel flow gallons / hr
        fuel_px = [0] * FG_MAX_ENGINES  # Fuel pressure psi
        egt = [0] * FG_MAX_ENGINES  # Exhuast gas temp deg F
        cht = [0] * FG_MAX_ENGINES  # Cylinder head temp deg F
        mp_osi = [0] * FG_MAX_ENGINES  # Manifold pressure
        tit = [0] * FG_MAX_ENGINES  # Turbine Inlet Temperature
        oil_temp = [0] * FG_MAX_ENGINES  # Oil temp deg F
        oil_px = [0] * FG_MAX_ENGINES  # Oil pressure psi

        # Consumables

        num_tanks = 0  # Max number of fuel tanks
        fuel_quantity = [0] * FG_MAX_TANKS  #

        # Gear status

        num_wheels = 0
        wow = [0] * FG_MAX_WHEELS
        gear_pos = [0]*FG_MAX_WHEELS
        gear_steer = [0] * FG_MAX_WHEELS
        gear_compression = [0] * FG_MAX_WHEELS

        # Environment

        cur_time = 0  # current unix time

        # FIXME: make this uint64_t before 2038

        warp = 0  # offset in seconds to unix time
        visibility = 0  # visibility in meters(for env.effects)

        # Control surface positions(normalized values)

        elevator = 0
        elevator_trim_tab = 0
        left_flap = 0
        right_flap = 0
        left_aileron = 0
        right_aileron = 0
        rudder = 0
        nose_wheel = 0
        speedbrake = 0
        spoilers = 0



    def htond(self,x):
        pass

    def htonf(self,x):
        pass

    def convertData(self):
        pass

