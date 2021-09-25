const roleHarvester = require('role.harvester');
const roleUpgrader = require('role.upgrader');
const roleBuilder = require('role.builder');

module.exports.loop = function () {
    // Eliminar screeps murtos de la memoria
    for(var name in Memory.creeps){
        if(!Game.creeps[name]){
            delete Memory.creeps[name];
        }
    }
    
    var harvesters = _.filter(Game.creeps, (creep) => creep.memory.role === 'harvester');
    var upgraders = _.filter(Game.creeps, (creep) => creep.memory.role === 'upgrader');
    var builders = _.filter(Game.creeps, (creep) => creep.memory.role === 'builder');
    
    if(harvesters.length < 3){
        if(Game.rooms['W8N3'].energyAvailable >= 200){
            var newName = 'Harvester' + Game.time;
            Game.spawns['Spawn1'].spawnCreep([WORK,WORK,CARRY,MOVE], newName,
                { memory: { 
                        role: 'harvester', 
                        working: true,
                        sourceID: '26f20772347f879'
                    }, 
                }
            );
        }
    }

    if (upgraders.length < 2) {
        if (Game.rooms['W8N3'].energyAvailable >= 200) {
            var newName = 'Upgrader' + Game.time;
            Game.spawns['Spawn1'].spawnCreep([WORK,WORK,CARRY,MOVE], newName,
                {
                    memory: {
                        role: 'upgrader',
                        working: true,
                        sourceID: '71ac0772347ffe6'
                    },
                }
            );
        }
    }

    if (builders.length < 3) {
        if (Game.rooms['W8N3'].energyAvailable >= 200) {
            var newName = 'Builder' + Game.time;
            console.log('Spawning new upgrader: ' + newName);
            Game.spawns['Spawn1'].spawnCreep([WORK,WORK,CARRY,MOVE], newName,
                { 
                    memory: { 
                        role: 'builder',
                        sourceID: '26f20772347f879'
                    }, 
                }
            );
        }
    }
    
    for(var name in Game.creeps){
        var creep = Game.creeps[name];
        if (creep.memory.role === 'undefined'){
            console.log(name)
        }
        if(creep.memory.role === 'harvester'){
            roleHarvester.run(creep);
        }
        if (creep.memory.role === 'upgrader') {
            roleUpgrader.run(creep);
        }
        if (creep.memory.role === 'builder') {
            roleBuilder.run(creep);
        }
    }
}