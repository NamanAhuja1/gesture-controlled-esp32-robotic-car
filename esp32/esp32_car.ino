// ===============================
// ESP32 Gesture Controlled Car
// Receives commands from Python
// via USB Serial
// ===============================

// Motor A
#define IN1 14
#define IN2 12

// Motor B
#define IN3 13
#define IN4 15

String command = "";

void setup() {

  Serial.begin(115200);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  stopCar();

  Serial.println("ESP32 Gesture Controlled Car Ready");
  Serial.println("Commands:");
  Serial.println("forward");
  Serial.println("backward");
  Serial.println("left");
  Serial.println("right");
  Serial.println("stop");
}

void loop() {

  if (Serial.available()) {

    command = Serial.readStringUntil('\n');
    command.trim();

    Serial.print("Received: ");
    Serial.println(command);

    if (command == "forward") {
      moveForward();
    }

    else if (command == "backward") {
      moveBackward();
    }

    else if (command == "left") {
      turnLeft();
    }

    else if (command == "right") {
      turnRight();
    }

    else if (command == "stop") {
      stopCar();
    }

    else {
      Serial.println("Unknown Command");
    }
  }
}

// =================================
// MOTOR FUNCTIONS
// =================================

void moveForward() {

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  Serial.println("Moving Forward");
}

void moveBackward() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  Serial.println("Moving Backward");
}

void turnLeft() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  Serial.println("Turning Left");
}

void turnRight() {

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  Serial.println("Turning Right");
}

void stopCar() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

  Serial.println("Stopped");
}
