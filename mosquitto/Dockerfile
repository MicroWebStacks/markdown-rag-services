# Use the official Eclipse Mosquitto image
FROM eclipse-mosquitto:latest

# Copy the custom Mosquitto configuration file into the image
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Ensure the config file has the correct permissions
RUN chown mosquitto:mosquitto /mosquitto/config/mosquitto.conf

# Set the entry point to use the custom configuration file
ENTRYPOINT ["/usr/sbin/mosquitto"]
CMD ["-c", "/mosquitto/config/mosquitto.conf"]
