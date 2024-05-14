const redis = require('redis');

class RedisClient{
/* handles interactions with redis server
 */
    constructor(){
        // create the redis client
        try{

            this.client= redis.createClient();
        } catch (err){
            console.error('Error creating Redis client:', err)
        }
        // handle error if any
        this.client.on('error', (err)=> console.error('Redis client Error:', err));
    }

    isAlive(){
        /* check if the connection is succesful
         */
        return this.client.connected;
    }

    async get(key){
        /*
         *Arg: key: this is the key to the value stored
         */
        try{
            return await this.client.get(key);
        } catch (err){
            console.error('Redis Get error:', err);
            return null || 'NOT FOUND';
        }
    }

    async set(key, value, duration){
        /*
         *used to set a string and its value
         *arg: key=> key to retrive the value
         * arg: value: this is the actual content
         * duration=> This is an integer to represent the period(sec) to store the value
         */
        try{
            await this.client.set(key, value, 'EX', duration);
        } catch(err){
            console.error('Redis Set error:', err)

        }
    }

    async del (key){
        /*used to delete an item using the provided key
         * arg: key=> this is the key used to retrieve an item from the db
         */
        try{
            await this.client.del(key);
        } catch(err){
            console.error('Redis delete error:', err);
        }

    }

}

const redisClient = new RedisClient();
module.exports = redisClient;
