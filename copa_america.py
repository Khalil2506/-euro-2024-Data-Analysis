import module as md
import pandas as pd 
import concat as ct
import LanusStats as ls

#fbref = ls.Fbref()
#player = fbref.get_player_season_stats('stats','Copa America','2024')
#player_america = pd.DataFrame(player) 

#df_player_america = ct.add_id_player_df(223,282,player_america)
match_america = md.match_competition(223,282)
# Usar la función para obtener el DataFrame de tarjetas amarillas por partido
tarjetas_amarillas_df = md.tarjetas_amarillas_por_partido(223, 282)
df_red = md.card_player(223, 282)
# Usar la función para obtener el DataFrame de oportunidades de gol por jugador
df_chance_goal = md.player_chance_goal(223, 282)
# Usar la función para obtener el DataFrame de dribles completos por partido
df_player_dribllle = md.player_dribble_complete(223, 282)
df_penalty_player = md.penalty_for_player(223,282)
df_pass_key = md.pass_key_for_matches(223, 282)
df_pass = md.pass_for_match(223, 282)
df_goal = md.goal_for_player(223, 282)
df_goal_player = df_goal.groupby(['player','country'])['goal'].sum().to_frame()
## Prueba la función
df_assist = md.assist_player(223, 282)
df_assist_player = df_assist.groupby(['player', 'country'])['assist'].sum().to_frame()
df_shot = md.shot_for_player(223, 282)
df_shot_player = df_shot.groupby(['player','country'])['shot'].count().to_frame()
df_port = md.porteria_zero(223, 282)
df_minutes = md.calcular_minutos_jugados(223,282)
df_match_for_player = md.calcular_partidos_jugados(223,282)
with pd.ExcelWriter('Copa_america_2024.xlsx') as writer:
    
    match_america.to_excel(writer,sheet_name='Match america', index=False)
    #df_player_america.to_excel(writer,sheet_name='Player america')
    df_pass.to_excel(writer, sheet_name='Pases', index=False)
    df_goal.to_excel(writer, sheet_name='Goles Por Jugador', index=False)
    df_assist.to_excel(writer, sheet_name='Asistencias Por Jugador', index=False)
    df_chance_goal.to_excel(writer, sheet_name='Oportunidades de Gol', index=False)
    df_player_dribllle.to_excel(writer, sheet_name='Dribles Completos', index=False)
    df_penalty_player.to_excel(writer, sheet_name='Penales Por Jugador', index=False)
    df_pass_key.to_excel(writer, sheet_name='Pases Clave', index=False)
    df_port.to_excel(writer, sheet_name='Porteria a cero', index=False)
    df_shot.to_excel(writer, sheet_name='Tiro por jugador', index=False)
    df_minutes.to_excel(writer, sheet_name='Minutos por jugador', index=False)
    df_match_for_player.to_excel(writer, sheet_name='partidos por jugador', index=False)
    tarjetas_amarillas_df.to_excel(writer, sheet_name='Tarjetas por Partido', index=False)
    df_red.to_excel(writer, sheet_name='Tarjetas por Jugador', index=False)