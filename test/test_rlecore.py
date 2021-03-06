"""The above testbench tests rle functioning and conversion"""

# @todo: this is temporary until `rle` parameters are updated
from argparse import Namespace as Constants

from myhdl import StopSimulation
from myhdl import block
from myhdl import ResetSignal, Signal, instance
from myhdl.conversion import verify

from jpegenc.subblocks.rle.rlecore import DataStream, rle, Pixel
from jpegenc.subblocks.rle.rlecore import RLESymbols, RLEConfig

from jpegenc.testing import toggle_signal, clock_driver, reset_on_start, pulse_reset
from rle_test_inputs import (red_pixels_1, green_pixels_1, blue_pixels_1,
                             red_pixels_2, green_pixels_2, blue_pixels_2,)


def block_process(
        constants, clock, block, datastream, rlesymbols, rleconfig, color):
    """This block sends data into rlecore and prints the output"""

    # select one among Y1,Y2 or Cb or Cr to be processes
    rleconfig.color_component.next = color

    # wait till start signal asserts
    yield toggle_signal(datastream.start, clock)

    # read input from the block
    datastream.input_val.next = block[rleconfig.read_addr]
    yield clock.posedge

    # read more inputs
    while rleconfig.read_addr != constants.max_write_cnt:
        datastream.input_val.next = block[rleconfig.read_addr]
        yield clock.posedge

        # print output
        if rlesymbols.dovalid:
            print("amplitude = %d runlength = %d size = %d" % (
                rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))

    datastream.input_val.next = block[rleconfig.read_addr]

    yield clock.posedge
    if rlesymbols.dovalid:
        print("amplitude = %d runlength = %d size = %d" % (
            rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))

    # extra clocks for all the inputs to process

    yield clock.posedge
    if rlesymbols.dovalid:
        print("amplitude = %d runlength = %d size = %d" % (
            rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))

    yield clock.posedge
    if rlesymbols.dovalid:
        print("amplitude = %d runlength = %d size = %d" % (
            rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))

    yield clock.posedge
    if rlesymbols.dovalid:
        print("amplitude = %d runlength = %d size = %d" % (
            rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))

    yield clock.posedge
    if rlesymbols.dovalid:
        print("amplitude = %d runlength = %d size = %d" % (
            rlesymbols.amplitude, rlesymbols.runlength, rlesymbols.size))


def test_rle_core():
    """We check the functionality here"""

    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=True)

    # constants for input, runlength, size width
    width = 6
    constants = Constants(width_addr=width, width_data=12,
                          max_write_cnt=63, rlength=4,
                          size=width.bit_length())
    pixel = Pixel()

    # interfaces to the rle core
    # input to the rle core and start signals sent from here
    datastream = DataStream(constants.width_data)

    # signals generated by the rle core
    rlesymbols = RLESymbols(
        constants.width_data,
        constants.size,
        constants.rlength)

    # selects the color component, manages address values
    rleconfig = RLEConfig(constants.max_write_cnt.bit_length())

    @block
    def bench_rle_core():
        """The RLE Core is tested in this block"""

        # instantiation of the rle core
        inst = rle(
            constants,
            reset, clock,
            datastream, rlesymbols, rleconfig
            )

        # clock instantiation
        inst_clock = clock_driver(clock)

        @instance
        def tbstim():

            # reset before sending data
            yield pulse_reset(reset, clock)

            # components of type Y1 or Y2 processed
            yield block_process(
                constants, clock,
                red_pixels_1, datastream, rlesymbols, rleconfig, pixel.Y1)

            print("======================")

            # components of type Y1 or Y2 processed
            yield block_process(
                constants,
                clock, red_pixels_2,
                datastream,
                rlesymbols,
                rleconfig, pixel.Y2
                )

            print("=====================")

            # components of type Cb processes
            yield block_process(
                constants,
                clock, green_pixels_1,
                datastream,
                rlesymbols,
                rleconfig, pixel.Cb
                )

            print ("=====================")

            # components od type Cb processed
            yield block_process(
                constants,
                clock, green_pixels_2,
                datastream,
                rlesymbols,
                rleconfig, pixel.Cb
                )

            print("=====================")

            # components of type Cr processed
            yield block_process(
                constants,
                clock, blue_pixels_1,
                datastream,
                rlesymbols,
                rleconfig, pixel.Cr
                )

            print("=====================")

            # components of type Cr processed
            yield block_process(
                constants,
                clock, blue_pixels_2,
                datastream,
                rlesymbols,
                rleconfig, pixel.Cr
                )

            print("=====================")

            # end of stream when sof asserts
            rleconfig.sof.next = True
            yield clock.posedge

            raise StopSimulation

        return tbstim, inst_clock, inst

    instance_rle = bench_rle_core()
    instance_rle.config_sim(trace=False)
    instance_rle.run_sim()


def test_rle_conversion():
    """This module checks for conversion"""
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=True)

    width = 6
    constants = Constants(width_addr=width, width_data=12,
                          max_write_cnt=63, rlength=4,
                          size=width.bit_length())

    datastream = DataStream(constants.width_data)
    rlesymbols = RLESymbols(
        constants.width_data, constants.size, constants.rlength)

    rleconfig = RLEConfig(constants.max_write_cnt.bit_length())

    @block
    def bench_rle_core():
        inst = rle(
            constants,
            reset, clock,
            datastream, rlesymbols, rleconfig
            )

        inst_clock = clock_driver(clock)
        inst_reset = reset_on_start(reset, clock)

        @instance
        def tbstim():

            yield clock.posedge
            print ("Conversion done!!")
            raise StopSimulation

        return tbstim, inst, inst_clock, inst_reset

    verify.simulator = 'iverilog'
    assert bench_rle_core().verify_convert() == 0
