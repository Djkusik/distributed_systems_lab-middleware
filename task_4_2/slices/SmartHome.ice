#ifndef SMART_HOME
#define SMART_HOME

module SmartHome
{
    exception DeviceException{};
    exception DeviceIsOffException extends DeviceException{};
    exception AlreadyTurnedOnException extends DeviceException{};
    exception AlreadyTurnedOffException extends DeviceException{};

    exception LackOfDataException{};

    interface Device {
        void turnOn() 
            throws AlreadyTurnedOnException;
        void turnOff() 
            throws AlreadyTurnedOffException;
    };

    struct OvenStatus {
        int heat;
        int humidity;
    };

    sequence<float> Readings;

    interface Oven extends Device {
        void heatUp (int heat) 
            throws DeviceIsOffException;
        void heatDown (int heat) 
            throws DeviceIsOffException;
        void humidityUp (int humidity) 
            throws DeviceIsOffException;
        void humidityDown (int humidity) 
            throws DeviceIsOffException;
        OvenStatus getStatus() 
            throws DeviceIsOffException;
    };

    interface Detector extends Device {
        float getReading() 
            throws LackOfDataException, DeviceIsOffException;
        Readings getAllReadings() 
            throws LackOfDataException, DeviceIsOffException;
    };

    interface HeatDetector extends Detector{};
    interface HumidityDetector extends Detector{};
    interface LightDetector extends Detector{};
};

#endif