const roleHarvester = require('role.harvester');
const roleUpgrader = require('role.upgrader');
const roleBuilder = require('role.builder');

module.exports.loop = function () {
    for(var name in Memory.creeps){
        if(!Game.creeps[name]){
            delete Memory.creeps[name];
        }
    }
    
    var harvesters = _.filter(Game.creeps, (creep) => creep.memory.role === 'harvester');
    var upgraders = _.filter(Game.creeps, (creep) => creep.memory.role === 'upgrader');
    var builders = _.filter(Game.creeps, (creep) => creep.memory.role === 'builder');
    
    if(harvesters.length < -3){
        if(Game.rooms['W7N2'].energyAvailable >= 200){
            var newName = 'Harvester' + Game.time;
            console.log('Spawning new upgrader: ' + newName);
            Game.spawns['Spawn1'].spawnCreep([WORK, CARRY, MOVE], newName,
                { memory: { role: 'harvester', extractEnergy: true }, });
        }
    }
    
    if(upgraders.length < 5){
        if(Game.rooms['W7N2'].energyAvailable >= 200){
            var newName = 'Upgrader' + Game.time;
            console.log('Spawning new upgrader: ' + newName);
            Game.spawns['Spawn1'].spawnCreep([WORK, CARRY, MOVE], newName,
                { memory: { role: 'upgrader', extractEnergy: true }, });
        }
    }
    
    if(builders.length < 2){
        if(Game.rooms['W7N2'].energyAvailable >= 200){
            var newName = 'Builder' + Game.time;
            console.log('Spawning new upgrader: ' + newName);
            Game.spawns['Spawn1'].spawnCreep([WORK, CARRY, MOVE], newName,
                { memory: { role: 'builder'}, });
        }
    }
    
    for(var name in Game.creeps){
        var creep = Game.creeps[name];
        if(creep.memory.role === 'harvester'){
            roleHarvester.run(creep);
        }
        if(creep.memory.role === 'upgrader'){
            roleUpgrader.run(creep);
        }
        if(creep.memory.role === 'builder'){
            roleBuilder.run(creep);
        }
    }
}