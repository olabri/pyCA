#!/bin/env python
# -*- coding: utf-8 -*-
import os

CAPTURE_AGENT_NAME  = 'PyCA'
IGNORE_TZ           = False
ADMIN_SERVER_URL    = 'http://example.com:8080'
ADMIN_SERVER_USER   = 'matterhorn_system_account'
ADMIN_SERVER_PASSWD = 'CHANGE_ME'
UPDATE_FREQUENCY    = 60
CAPTURE_DIR         = '%s/recordings' % os.path.dirname(os.path.abspath(__file__))
CAPTURE_PLUGIN      = 'ffmpeg-v4l-alsa'

# Setting this to true will cause the pyCA to not register itself or ingest
# stuff to the admin server. It's useful if you want it as cbackup to another
# CA to just get the files manually if the regular CA fails.
BACKUP_AGENT        = False

########################################################################
## Capture configuration                                               #
########################################################################

# Specify any command you like to use for capturing. You can also execute a
# shell script if you want to. The only thing that is important is that the
# command has to terminate itself in time.
#
# Possible string substitutions you can use are:
# ==============================================
#
#   %(time)s     Time to capture in seconds
#   %(recdir)s   Directory to put recordings in
#   %(recname)s  Autogenerated name of the recording.
#
# Examples:
# =========
#
# Record audio only using FFmpeg:
# -------------------------------
#
# CAPTURE_COMMAND = '''ffmpeg -f alsa -ac 1 -i hw:1 -t %(time)s -c:a flac -ac 1 \
#   -c:v libx264 -preset ultrafast -qp 0 %(recdir)s/%(recname)s.flac'''
#
#
# Record video4linux2 and alsa source:
# ------------------------------------
#
# CAPTURE_COMMAND = '''ffmpeg -f v4l2 -s 1280x720 -i /dev/video1 \
#   -f alsa -ac 1 -i hw:1 -t %(time)s -c:a flac -ac 1 \
#   -c:v libx264 -preset ultrafast -qp 0 %(recdir)s/%(recname)s.mkv'''
#
#
# Record video on a Reaspberry Pi using the camera module:
# --------------------------------------------------------
#
# CAPTURE_COMMAND = '''raspivid -n -t %(time)s000 -b 4000000 -fps 30 -o - | \
#   ffmpeg -r 30 -i pipe:0 -c:v copy %(recdir)s/%(recname)s.mp4'''
#
#
# Record audio using arecord:
# ---------------------------
#
# CAPTURE_COMMAND = '''arecord -c 2 -d %(time)s -r 44100 -f S16_LE -D hw:0 \
#   %(recdir)s/%(recname)s.mp4'''
#
#
# Record video and audio on a Reaspberry Pi using the camera module:
# ------------------------------------------------------------------
#
# CAPTURE_COMMAND = '''raspivid -t %(time)s000 -b 4000000 -fps 30 -o - | \
#   ffmpeg -ac 1 -f alsa -i plughw:1 \
#   -r 25 -i pipe:0 \
#   -filter:a aresample=async=1 \
#   -c:a flac -c:v copy \
#   -t %(time)s -y %(recdir)s/%(recname)s.mp4'''
#
CAPTURE_COMMAND = '''ffmpeg -re -f lavfi -r 25 -i testsrc \
		-t %(time)s -map 0:v %(recdir)s/%(recname)s.mp4 \
		-t %(time)s -map 0:v -filter:v select='not(mod(n\,50))' \
			-updatefirst 1 %(recdir)s/preview.jpg'''

# Specify the names of the output files as well as their flavor. Multiple
# output files can be specified. The same string substitutions can be made as
# with the capture command.
CAPTURE_OUTPUT = [('presenter/source', '%(recdir)s/%(recname)s.mp4')]

# Specify a preview image to show in the web UI. If no image is specified, none
# is shown. Multiple images can be specified. The only string substitution
# ehich can be used in here is %(recdir)s.
CAPTURE_PREVIEW = ['%(recdir)s/preview.jpg']

CAPTURE_UI_USER = 'admin'
CAPTURE_UI_PASSWD = 'opencast'
