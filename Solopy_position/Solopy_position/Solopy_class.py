import Solopy as solo

import time

class SoloPMSM():
	
	def __init__(self):

		self.Connection(self.Instantiate())

	def Instantiate(self):

		mySolo = solo.SoloMotorControllerUart("/dev/ttyACM0", 0, solo.UART_BAUD_RATE.RATE_937500) # 1.시리얼 포트 지정 2.모터 컨트롤러 ID 3.시리얼 통신의 속도

		return mySolo

	def Connection(self, mySolo): # 모터 커넥션 확인
	
		print("Trying to Connect To SOLO")
		connection_is_working = False

		while connection_is_working is False:
			time.sleep(1)
			connection_is_working, error = mySolo.connection_is_working()
		print("Communication Established successfully!")
	
	def Configuration(self, mySolo, pwmFrequency, currentLimit, numberOfPoles, numberOfEncoderLines, speedControllerKp, speedControllerKi, positionControllerKp, positionControllerKi):

		# 모터와 디바이스의 초기 구성
		mySolo.set_output_pwm_frequency_khz(pwmFrequency)
		mySolo.set_current_limit(currentLimit)
		mySolo.set_motor_poles_counts(numberOfPoles)
		mySolo.set_incremental_encoder_lines(numberOfEncoderLines)
		mySolo.set_command_mode(solo.COMMAND_MODE.DIGITAL)
		mySolo.set_motor_type(solo.MOTOR_TYPE.BLDC_PMSM)

		# 모터ID 식별
		mySolo.motor_parameters_identification(solo.ACTION.START)
		print("Identifying the Motor")

		time.sleep(2)

		# Operate while using Quadrature Incremental Encoders
		mySolo.set_feedback_control_mode(solo.FEEDBACK_CONTROL_MODE.ENCODERS)
		mySolo.set_control_mode(solo.CONTROL_MODE.POSITION_MODE)
		# Speed Controller Tunings
		mySolo.set_speed_controller_kp(speedControllerKp)
		mySolo.set_speed_controller_ki(speedControllerKi)
		# Position Controller Tunings
		mySolo.set_position_controller_kp(positionControllerKp)
		mySolo.set_position_controller_ki(positionControllerKi)

	def Loop_action(self, mySolo, desiredSpeedLimit, desiredPositionRefer): # Reference Position에 도달하기 위한 함수. set은 함수 실행 시 한 번만, get은 루프를 통해 지속적 피드백

		mySolo.set_speed_limit(desiredSpeedLimit)

		mySolo.set_position_reference(desiredPositionRefer)

		time.sleep(1)

		while True:

			actualMotorSpeed = mySolo.get_speed_feedback()

			print("Motor Speed [RPM]: " + str(actualMotorSpeed))

			time.sleep(8)

			actualMotorPosition, error = mySolo.get_position_counts_feedback()
			print("Number of Pulses passed: " + str(actualMotorPosition))

			if error < 0.001:
				break
			# Reference Position error가 0.001보다 작으면 탈출

	def Disconnect(self, mySolo): # 시리얼 종료

		mySolo.disconnect()




