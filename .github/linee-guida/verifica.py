#!/usr/bin/env python3
"""Controllo di conformità alle linee guida (gestito dalla sincronizzazione del registro-delle-idee).

Errori (bloccanti): file obbligatori mancanti, file di ingresso senza rimandi, STATO.md incompleto.
Avvisi (non bloccanti): struttura delle cartelle diversa dallo standard.
Un punto citato nella sezione '## [Gian] Deroghe alle linee guida' di AGENTS.md non viene segnalato.
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'

def read(name):
    p = os.path.join(ROOT, name)
    return open(p, encoding='utf-8').read() if os.path.isfile(p) else None

agents = read('AGENTS.md') or ''
m = re.search(r'^## \[Gian\] Deroghe alle linee guida.*?(?=^## |\Z)', agents, re.S | re.M)
deroghe = m.group(0) if m else ''

def derogato(chiave):
    return chiave in deroghe

errori, avvisi = [], []

def errore(chiave, testo):
    if not derogato(chiave):
        errori.append(testo)

linee = read('LINEE_GUIDA.md')
if linee is None:
    errore('LINEE_GUIDA.md', 'manca LINEE_GUIDA.md')
elif not re.search(r'<!-- linee-guida-versione: (\d+\.\d+\.\d+) -->', linee):
    errore('LINEE_GUIDA.md', 'LINEE_GUIDA.md non contiene la riga di versione')

for nome in ('README.md', 'AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'STATO.md', '.github/copilot-instructions.md'):
    if read(nome) is None:
        errore(nome, f'manca {nome}')

if not any(read(n) is not None for n in ('LICENSE', 'LICENSE.md', 'RIGHTS_NOTICE.md', 'COPYRIGHT.md')):
    errore('diritti', 'manca un file sui diritti (LICENSE, RIGHTS_NOTICE.md o COPYRIGHT.md)')

if agents and '<!-- inizio-protocollo-comune -->' not in agents:
    errore('AGENTS.md', 'AGENTS.md non contiene la sezione [Gian] Protocollo comune')
claude = read('CLAUDE.md') or ''
if claude and '@LINEE_GUIDA.md' not in claude:
    errore('CLAUDE.md', 'CLAUDE.md non importa @LINEE_GUIDA.md')
readme = read('README.md') or ''
if readme and '<!-- inizio-riquadro-linee-guida -->' not in readme:
    errore('README.md', 'README.md non contiene il riquadro delle linee guida')

stato = read('STATO.md') or ''
if stato:
    for sezione in ("Cos'è", 'Fase', 'Dove è pubblicata', 'Prossimi passi', 'Blocchi', 'Componenti condivisi', 'Registro aggiornamenti'):
        if not re.search(r'^## ' + re.escape(sezione), stato, re.M):
            errore('STATO.md', f'STATO.md: manca la sezione "{sezione}"')

import subprocess
try:
    tracciati = set(subprocess.run(['git', '-C', ROOT, 'ls-files'], capture_output=True, text=True, check=True).stdout.split('\n'))
except Exception:
    tracciati = None
for nome in ('.env', '.env.local', '.env.production'):
    presente = (nome in tracciati) if tracciati is not None else os.path.isfile(os.path.join(ROOT, nome))
    if presente and not derogato(nome):
        errori.append(f'{nome} non deve essere nel repository')

standard = {'app', 'server', 'shared', 'tests', 'scripts', 'docs', 'assets', 'worker', 'apps', 'packages', 'services',
            'components', 'hooks', 'lib', 'modules', 'ios', 'android', 'public', 'includes', 'src', 'test', 'tools'}
for voce in sorted(os.listdir(ROOT)):
    p = os.path.join(ROOT, voce)
    if os.path.isdir(p) and not voce.startswith('.') and voce not in standard and voce != 'node_modules' and not derogato(voce + '/'):
        avvisi.append(f'cartella "{voce}/" fuori dallo standard (ammessa per i repository nati prima della v1.0)')

for a in avvisi:
    print(f'::warning::{a}')
for e in errori:
    print(f'::error::{e}')
print(f'Linee guida: {len(errori)} errori, {len(avvisi)} avvisi.')
sys.exit(1 if errori else 0)
