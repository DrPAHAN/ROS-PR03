# ROS-PR03
# PR03 — patrol

Нода на rclpy: подписка на /turtle1/pose, таймер 0.1 с, публикация geometry_msgs/msg/Twist.

## Сборка

source /opt/ros/lyrical/setup.bash
colcon build --symlink-install --packages-select patrol
source install/setup.bash

## Тесты

colcon test --packages-select patrol --event-handlers console_direct+
colcon test-result --verbose

## Запуск

Терминал 1:
ros2 run turtlesim turtlesim_node

Терминал 2 (исправленное имя топика через remap):
ros2 run patrol patrol --ros-args -r cmd_vel:=/turtle1/cmd_vel

Терминал 3 (проверка):
ros2 topic info /turtle1/cmd_vel --verbose
ros2 topic hz /turtle1/cmd_vel

## Дефект и исправление

Без remap нода публикует в /patrol/cmd_vel (относительное имя cmd_vel),
а turtlesim слушает /turtle1/cmd_vel. Связи нет.
Remap cmd_vel:=/turtle1/cmd_vel восстанавливает доставку.
