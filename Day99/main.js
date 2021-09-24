const roleHarvester = require('role.harvester');

module.exports.loop = function () {
    // Eliminar screeps murtos de la memoria
    for(var name in Memory.creeps){
        if(!Game.creeps[name]){
            delete Memory.creeps[name];
        }
    }
    
    var harvesters = _.filter(Game.creeps, (creep) => creep.memory.role === 'harvester');
    
    if(harvesters.length < 3){
        if(Game.rooms['W8N3'].energyAvailable >= 200){
            var newName = 'Harvester' + Game.time;
            console.log('Spawning new upgrader: ' + newName);
            Game.spawns['Spawn1'].spawnCreep([WORK,WORK,CARRY,MOVE], newName,
                { memory: { 
                        role: 'harvester', 
                        working: true,
                        sourceID: '71ac0772347ffe6'
                    }, 
                }
            );
        }
    }
    
    for(var name in Game.creeps){
        var creep = Game.creeps[name];
        if(creep.memory.role === 'harvester'){
            roleHarvester.run(creep);
        }
    }
}