import SmartHome.*;

import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Util;
import com.zeroc.Ice.ObjectPrx;
import com.zeroc.Ice.LocalException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Client {
    static ArrayList<String> devices = new ArrayList<String>() {
        {
            add("Oven");
            add("HeatDetector");
            add("HumidityDetector");
            add("LightDetector");
        }
    };

    public static void main(String[] args) {
        int status = 0;
        Communicator ic = null;
        ic = Util.initialize(args);
        String[] cmd = null;
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.print("CMD> ");
            try {
                cmd = in.readLine().split(" ");
            } catch (IOException e) {
                e.printStackTrace();
                status = 1;
            }

            ObjectPrx base = null;
            if (devices.contains(cmd[0])) {
                base = ic.stringToProxy("SmartHome/" + cmd[0] + ":default -h localhost -p 10000");
            }

            if (cmd[0].equals("help")) {
                printHelp();
            } else if (cmd[0].equals("quit")) {
                break;
            } else if (base == null) {
                System.out.println("Wrong device");
            } else {
                try {
                    execute(cmd, base);
                } catch (LocalException e) {
                    e.printStackTrace();
                    status = 1;
                } catch (DeviceException | LackOfDataException e) {
                    System.err.println(e.toString());
                    continue;
                } catch (Exception e) {
                    System.err.println(e.getMessage());
                    status = 1;
                }
            }
        }

        if (ic != null) {
            try {
                ic.destroy();
            } catch (Exception e) {
                System.err.println(e.getMessage());
                status = 1;
            }
        }
        System.exit(status);
    }

    static private void execute(String[] cmd, ObjectPrx base) throws Exception {
        switch(cmd[0]) {
            case "Oven":
                OvenPrx oven = OvenPrx.checkedCast(base);
                evalOven(oven, cmd);
                break;
            case "HeatDetector":
                HeatDetectorPrx heatDetector = HeatDetectorPrx.checkedCast(base);
                evalHeatDetector(heatDetector, cmd);
                break;
            case "HumidityDetector":
                HumidityDetectorPrx humidityDetector = HumidityDetectorPrx.checkedCast(base);
                evalHumidityDetector(humidityDetector, cmd);
                break;
            case "LightDetector":
                LightDetectorPrx lightDetector = LightDetectorPrx.checkedCast(base);
                evalLightDetector(lightDetector, cmd);
                break;
        }
    }

    static private String[] getCmd(BufferedReader in) throws Exception {
        while (true) {
            System.out.print("DEVICE_CMD> ");
            String[] cmd = in.readLine().split(" ");
            return cmd;
        }
    }

    static private void evalOven(OvenPrx oven, String[] cmd) throws Exception {
        switch(cmd[1]) {
            case "turnOn":
                oven.turnOn();
                System.out.println("Oven turned on");
                break;
            case "turnOff":
                oven.turnOff();
                System.out.println("Oven turned off");
                break;
            case "heatUp":
                oven.heatUp(Integer.valueOf(cmd[2]));
                System.out.println("Oven heated up by: " + cmd[2]);
                break;
            case "heatDown":
                oven.heatDown(Integer.valueOf(cmd[2]));
                System.out.println("Oven heated down by: " + cmd[2]);
                break;
            case "humidityUp":
                oven.humidityUp(Integer.valueOf(cmd[2]));
                System.out.println("Oven humidity up by: " + cmd[2]);
                break;
            case "humidityDown":
                oven.humidityDown(Integer.valueOf(cmd[2]));
                System.out.println("Oven humidity down by: " + cmd[2]);
                break;
            case "getStatus":
                OvenStatus status = oven.getStatus();
                System.out.println("Oven heat: " + String.valueOf(status.heat));
                System.out.println("Oven humidity: " + String.valueOf(status.humidity));
                break;
            default:
                System.out.println("Unknown command");
        }
    }

    static private void evalHeatDetector(HeatDetectorPrx heatDetector, String[] cmd) throws Exception {
        switch(cmd[1]) {
            case "turnOn":
                heatDetector.turnOn();
                System.out.println("HeatDetector turned on");
                break;
            case "turnOff":
                heatDetector.turnOff();
                System.out.println("HeatDetector turned off");
                break;
            case "getReading":
                float value = heatDetector.getReading();
                System.out.println("Last HeatDetector value: " + String.valueOf(value));
                break;
            case "getAllReadings":
                float[] values = heatDetector.getAllReadings();
                System.out.println("HeatDetector all values: ");
                for (float val : values) {
                    System.out.println("\t" + String.valueOf(val));
                }
                break;
            default:
                System.out.println("Unknown command");
        }
    }

    static private void evalHumidityDetector(HumidityDetectorPrx humidityDetector, String[] cmd) throws Exception {
        switch(cmd[1]) {
            case "turnOn":
                humidityDetector.turnOn();
                System.out.println("HumidityDetector turned on");
                break;
            case "turnOff":
                humidityDetector.turnOff();
                System.out.println("HumidityDetector turned off");
                break;
            case "getReading":
                float value = humidityDetector.getReading();
                System.out.println("Last HumidityDetector value: " + String.valueOf(value));
                break;
            case "getAllReadings":
                float[] values = humidityDetector.getAllReadings();
                System.out.println("HumidityDetector all values: ");
                for (float val : values) {
                    System.out.println("\t" + String.valueOf(val));
                }
                break;
            default:
                System.out.println("Unknown command");
        }
    }

    static private void evalLightDetector(LightDetectorPrx lightDetector, String[] cmd) throws Exception {
        switch(cmd[1]) {
            case "turnOn":
                lightDetector.turnOn();
                System.out.println("LightDetector turned on");
                break;
            case "turnOff":
                lightDetector.turnOff();
                System.out.println("LightDetector turned off");
                break;
            case "getReading":
                float value = lightDetector.getReading();
                System.out.println("Last LightDetector value: " + String.valueOf(value));
                break;
            case "getAllReadings":
                float[] values = lightDetector.getAllReadings();
                System.out.println("LightDetector all values: ");
                for (float val : values) {
                    System.out.println("\t" + String.valueOf(val));
                }
                break;
            default:
                System.out.println("Unknown command");
        }
    }

    static private void listDevices() {
        System.out.println("Devices: ");
        for (String device : devices) {
            System.out.println("\t> " + device);
        }
    }

    static private void printHelp() {
        System.out.println("\t\t\t\t\t\t***HELP***");
        listDevices();
        System.out.println("For every device: ");
        System.out.println("\tDevice command <arguments> - this is correct form of command");
        System.out.println("\tturnOn - turning device on");
        System.out.println("\tturnOff - turning device off");
        System.out.println("Oven: ");
        System.out.println("\t[heat|humidity]Up <value> - increase heat or humidity by value");
        System.out.println("\t[heat|humidity]Down <value> - decrease heat or humidity by value");
        System.out.println("\tgetStatus - get current status of oven");
        System.out.println("Detectors: ");
        System.out.println("\tgetReading - prints last reading");
        System.out.println("\tgetAllReadings - prints all readings");
        System.out.println("************************************************************************************");
    }
}
