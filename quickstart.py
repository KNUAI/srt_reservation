""" Quickstart script for InstaPy usage """

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

if __name__ == "__main__":
    cli_args = parse_cli_args()

    login_id = config['login_id']
    login_psw = config['login_psw']
    dpt_stn = config['dpt_stn']
    arr_stn = config['arr_stn']
    dpt_dt = config['dpt_dt']
    dpt_tm = config['dpt_tm']

    num_trains_to_check = config['num_trains_to_check']
    want_special = config['want_special']
    want_reserve = config['want_reserve']

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, num_trains_to_check, want_special, want_reserve)
    srt.run(login_id, login_psw)