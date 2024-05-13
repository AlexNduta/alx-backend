const { createClient } = require('redis');

class RedisClient {
  constructor() {
    this.client = createClient(); // Create the Redis client
    this.client.on('error', (err) => {
      console.error('Redis Client Error:', err);
    });
  }

  async isAlive() {
    /*
     * Returns true if the connection to Redis is successful, otherwise false.
     */
    try {
      await this.client.connected; // Attempt connection
      return true;
    } catch (err) {
      console.error('Redis Connection Error:', err);
      return false;
    }
  }

  async get(key) {
    try {
      const value = await this.client.get(key); // Get value for key
      return value;
    } catch (err) {
      console.error('Redis Get Error:', err);
      return null; // Indicate error by returning null
    }
  }

  async set(key, value, duration) {
    try {
      // Set key-value pair with expiration
      await this.client.set(key, value, 'EX', duration);
    } catch (err) {
      console.error('Redis Set Error:', err);
    }
  }

  async del(key) {
    try {
      await this.client.del(key); // Delete key-value pair
    } catch (err) {
      console.error('Redis Delete Error:', err);
    }
  }
}

const redisClient = new RedisClient();
module.exports = redisClient;
