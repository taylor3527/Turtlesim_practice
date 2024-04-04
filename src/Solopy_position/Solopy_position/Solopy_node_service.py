import rclpy
from rclpy.node import Node
from Solopy_class import SoloPMSM

from solopy_msg.msg import Props


if __name__ == '__main__':

    msg = Props()

    [msg.pwm, msg.nop, msg.noe, msg.skp, msg.ski, msg.pkp, msg.pki, msg.cl, msg.busvol, msg.dsl, msg.dpr] = [20, 8, 1000, 0.1, 0.008, 0.12, 0.02, 7.5, 0, 1000, 0]

    #[pwmFrequency, numberOfPoles, numberOfEncoderLines, speedControllerKp, speedControllerKi, positionControllerKp, positionControllerKi, currentLimit, busVoltage, desiredSpeedLimit, desiredPositionRefer]

    Msg = [msg.pwm, msg.nop, msg.noe, msg.skp, msg.ski, msg.pkp, msg.pki, msg.cl, msg.busvol, msg.dsl, msg.dpr]

    MySolo.Configuration(mySolo, Msg[0], Msg[7], Msg[1], Msg[2], Msg[3], Msg[4], Msg[5], Msg[6])

    MySolo.Loop_action(mySolo, Msg[9], Msg[10])

    MySolo.Disconnect(mySolo)

    


