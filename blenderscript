import bpy
import mathutils

# Seleciona o objeto atual
obj = bpy.context.active_object

# Armazena a posição do objeto principal
pos = obj.location

# Define o número de objetos que serão criados
num_obj = 8

# Define a distância entre os objetos
distance = 2.0

# Define a matriz de posições
positions = [
    mathutils.Vector((pos.x - distance, pos.y + distance, pos.z)),
    mathutils.Vector((pos.x, pos.y + distance, pos.z)),
    mathutils.Vector((pos.x + distance, pos.y + distance, pos.z)),
    mathutils.Vector((pos.x - distance, pos.y, pos.z)),
    mathutils.Vector((pos.x + distance, pos.y, pos.z)),
    mathutils.Vector((pos.x - distance, pos.y - distance, pos.z)),
    mathutils.Vector((pos.x, pos.y - distance, pos.z)),
    mathutils.Vector((pos.x + distance, pos.y - distance, pos.z))
]

# Loop para criar vários objetos
for i in range(num_obj):
    
    # Cria uma cópia do objeto
    new_obj = obj.copy()
    
    # Adiciona o objeto à cena
    bpy.context.scene.objects.link(new_obj)
    
    # Define a posição do objeto copiado
    new_obj.location = positions[i]
    
# Exporta o arquivo HTML
bpy.ops.export_scene.b4w_html(filepath="C:/desenv/ProjetoEspecializado/malha.html")
