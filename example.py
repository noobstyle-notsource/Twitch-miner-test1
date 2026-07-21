# -*- coding: utf-8 -*-

import logging
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Settings import Priority, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, Condition, OutcomeKeys, FilterCondition, DelayMode
from TwitchChannelPointsMiner.classes.entities.Streamer import Streamer, StreamerSettings

twitch_miner = TwitchChannelPointsMiner(
    username="noobstyle0885",
    password="Trollheh123...",                  # Securely passed to bypass interactive mode prompts
    claim_drops_startup=False,                  # Skips bulk inventory claims during initialization
    priority=[                                  # Focuses system resources automatically by function
        Priority.STREAK,                        # Priority 1: Secure daily consecutive watch streaks
        Priority.DROPS,                         # Priority 2: Mine drops from enabled campaigns
        Priority.ORDER                          # Priority 3: Fall back to channel list sequence
    ],
    enable_analytics=False,                     # Saved False to fit within free tier RAM thresholds
    disable_ssl_cert_verification=False,        
    disable_at_in_nickname=False,               
    logger_settings=LoggerSettings(
        save=True,                              # Keeps an automated diagnostic log archive
        console_level=logging.INFO,             # Displays concise execution events to terminal
        console_username=False,                 
        auto_clear=True,                        # Auto-purges old logs after seven operational days
        time_zone="",                           
        file_level=logging.DEBUG,               
        emoji=True,                             
        less=False,                             
        colored=True,                           
        color_palette=ColorPalette(             
            STREAMER_online="GREEN",            
            streamer_offline="red",             
            BET_wiN=Fore.MAGENTA                
        ),
        # Disconnected unused configuration modules to prevent broken dependency warnings
        telegram=None,
        discord=None,
        webhook=None,
        matrix=None,
        pushover=None,
        gotify=None
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,                  # Participates in stream prediction mini-games
        follow_raid=True,                       # Hops raids with stream hosts for +250 points
        claim_drops=True,                       # Keeps tracking active toward in-game drops
        claim_moments=True,                     # Claims user moments instantly when they trigger
        watch_streak=True,                      # Signals priority shift when streak windows open
        community_goals=False,                  
        chat=ChatPresence.ONLINE,               # Connects to Twitch IRC chat system rooms
        bet=BetSettings(
            strategy=Strategy.SMART,            # Weighs crowd sizes against best-paying multipliers
            percentage=5,                       # Limits exposure per prediction to 5% of stack
            percentage_gap=20,                  
            max_points=50000,                   
            stealth_mode=True,                  # Deducts 1-2 points from cap to stay under radar
            delay_mode=DelayMode.FROM_END,      
            delay=6,                            # Places bets 6 seconds before final timer cutoff
            minimum_points=20000,               # Halts betting if bank pool drops below this floor
            filter_condition=FilterCondition(
                by=OutcomeKeys.TOTAL_USERS,
                where=Condition.LTE,
                value=800                       # Restricts bets to pools under 800 total users
            )
        )
    )
)

# Executes the engine across your entire active profile followers pool
twitch_miner.mine(
    followers=True, 
    followers_order=FollowersOrder.ASC
)
