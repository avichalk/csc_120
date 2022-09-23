# Word of the day - there wasn't one? i thought i'd missed it during the lecture but i watched the entire thing again and prof. Russ just never gave us one I think.

# Activity 1
'''
We can store all the sprites in a linked list. We can insert out pointer
at any given position in the linked list and move forward for each subsequent
frame of movement.
When it gets stepped on, we can call a subroutine to change its sprite and disable
it for a short period of time. This also applies to the fireball, where we can call
a subroutine to kill the goomba. If it runs into another enemy of the same type, we
can have it ignore the collision. Or, we could have different hitboxes for enemies
and mario, so the hitboxes for the enemies only apply to mario (not other enemies) and
the hitbox for mario applies only to enemies (so there's no friendly fire in multiplayer mode)
goomba.stomped()
goomba.dead()
goomba.advance_sprite()
goomba.sprites
goomba.position
'''

# Activity 2
'''
The only difference I can think off is an attack mode, dependent on the position of the enemy.
goomba.mario_pos()
goomba.attack_mario()
'''

# Activity 3
'''
When it get stepped on, we can update the sprite and keep a timer for how long it is supposed to
remain stomped. We can also disable its hitbox for mario for that time. When it is done being
stomped we let it resume its functionality after calling a waking up animation.
'''

# Activity 4
'''
Firstly- is the block interactible, so can you hit its sprite and expect something to happen
(except the block disintegrating). We should also make proper hitboxes for the box. We should
check its x and y positions and insert it accordingly.
'''

# Activity 5
'''
The interactivity field will be mostly the same- if the hitboxes overlap, an interaction happens.
The display fields are almost the same, except the goombas move and the blocks don't (unless they
are interactable).
'''

# Activity 6
'''
We can store everything in a 'room' object. The rooms are loaded and deloaded as mario enters or leaves
them. These rooms can have pointers to next rooms, the positions of enemies, blocks and obstacles,
The pipes will also have references leading to other rooms, the size of the room, etc. The levels can be
given the pointers for the rooms that the level is supposed to start in.
'''