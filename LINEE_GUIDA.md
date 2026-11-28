<!-- linee-guida-versione: 1.1.0 -->
# Linee guida dei progetti di Gian Paolo Franceschini — v1.1.0

> **Questo è il primo documento da leggere** in qualsiasi repository di Gian, per persone e per AI (ChatGPT/Codex, Claude, Gemini, Copilot e qualsiasi altro agente).
> L'originale vive in `gianpaolobol/registro-delle-idee/LINEE_GUIDA.md`. Nei singoli repository c'è una **copia sincronizzata automaticamente**: non modificarla lì, perché verrebbe sovrascritta. Le modifiche si fanno solo nell'originale.
> In caso di conflitto valgono, in quest'ordine: 1) una decisione esplicita di Gian; 2) le **deroghe** firmate `[Gian]` nell'`AGENTS.md` del repository; 3) queste linee guida; 4) le altre istruzioni del repository.

---

## 1. Da idea a progetto

1. **Ogni idea nasce nel registro** (`registro-delle-idee/REGISTRO_IDEE.md`), con il modello `modelli/IDEA.md`. Non si apre un repository per un'idea.
2. **Un'idea diventa progetto solo quando lo decide Gian.** Allora:
   - si crea il repository con nome in minuscolo con trattini (`penna-viva`, `fungo-italia`);
   - si copia dentro il contenuto di `modello-progetto/` del registro: nasce già conforme all'ultima versione di queste linee guida;
   - la prima pull request compila `STATO.md` e aggiorna nel registro la scheda dell'idea (stato `progetto` con il link) e la riga in `STATO_APP.md`;
   - il repository va aggiunto all'elenco `repository.txt` del registro, così riceve gli aggiornamenti delle linee guida.

## 2. Struttura standard di un repository

### 2.1 File obbligatori nella radice

| File | Contenuto | Chi lo modifica |
|---|---|---|
| `LINEE_GUIDA.md` | Copia di questo documento | Solo la sincronizzazione automatica |
| `README.md` | Riquadro iniziale "Linee guida", cos'è il progetto, come avviarlo | Tutti |
| `AGENTS.md` | Istruzioni per le AI: protocollo comune in cima, poi sezioni firmate e **deroghe** | Tutti, solo aggiungendo (cap. 4) |
| `CLAUDE.md` | `@LINEE_GUIDA.md` e `@AGENTS.md`, più eventuali istruzioni solo per Claude | Tutti, solo aggiungendo |
| `GEMINI.md` | `@./LINEE_GUIDA.md` e `@./AGENTS.md` | Solo la sincronizzazione |
| `STATO.md` | Stato del progetto in una pagina (cap. 5) | Chi finisce un lavoro |
| Diritti | `LICENSE` oppure `RIGHTS_NOTICE.md` / `COPYRIGHT.md`: codice proprietario salvo decisione diversa di Gian | Solo Gian |
| `.gitignore` | Esclude segreti, build, dipendenze | Tutti |
| `.env.example` | Solo i **nomi** delle variabili d'ambiente, mai i valori | Tutti (se il progetto usa variabili) |

E inoltre, gestiti dalla sincronizzazione: `.github/copilot-instructions.md` (rimando per GitHub Copilot), `.github/workflows/verifica-linee-guida.yml` e `.github/linee-guida/verifica.py` (controllo automatico).

### 2.2 Cartelle standard

| Cartella | Contenuto |
|---|---|
| `app/` | Applicazione client (mobile, web, desktop) |
| `server/` | Backend, API, worker |
| `shared/` | Codice condiviso tra app e server, o da riusare in altri progetti |
| `tests/` | Test automatici |
| `scripts/` | Strumenti di sviluppo, build, migrazione |
| `docs/` | Documentazione lunga: decisioni (`docs/decisioni/`), passaggi di consegne, prove |
| `assets/` | Immagini, icone, font |
| `.github/` | Workflow e istruzioni per GitHub |

Si creano solo le cartelle che servono.

**Eccezioni già ammesse senza deroga**, quando le impone lo strumento usato:
- Expo / React Native: `App.tsx`, `index.ts`, `app.json` / `app.config.*`, `eas.json` nella radice; cartelle `components/`, `hooks/`, `lib/`, `modules/` ammesse al posto di `app/`.
- Capacitor: `ios/`, `android/`, `capacitor.config.json`.
- PHP su hosting condiviso: le pagine pubbliche nella radice o in `public/`; `includes/` per il codice comune.
- Cloudflare Workers: `worker/` al posto di `server/`, `wrangler.*` nella radice.
- Monorepo esistenti con `apps/`, `packages/`, `services/`.

**Repository nati prima della v1.0:** non si spostano file già esistenti per rispettare le cartelle; questo rischia di rompere build e pubblicazioni. Valgono subito i file obbligatori e le regole; le cartelle si adeguano solo per il codice nuovo o quando Gian lo decide.

## 3. Regole di lavoro

1. **Branch dedicato** per ogni intervento: `feat/…`, `fix/…`, `docs/…`, `audit/…`, `chore/…`.
2. **Pull request** verso `main`. Push diretto su `main` solo se Gian l'ha autorizzato per quel repository con una deroga.
3. Nella PR: cosa cambia, **quali test sono stati eseguiti davvero**, cosa non è stato verificato.
4. Codice importante (login, pagamenti, dati personali, sicurezza, rilasci): **revisione incrociata** da un'altra AI prima dell'integrazione.
5. Non sovrascrivere il lavoro di un'altra AI: se c'è una PR aperta sugli stessi file, commentala.
6. **Riuso prima di tutto**: controlla `registro-delle-idee/MAPPA_COLLEGAMENTI.md`. Se riusi codice di un altro repository, nel commit scrivi `origine: <repo>@<commit> <percorso>`. Se crei o migliori un componente riusabile, aggiorna la mappa.
7. **Stati da non confondere**: implementato ≠ testato ≠ revisionato ≠ pubblicato. "Pubblicato" solo con un link verificabile.
8. **Sicurezza**: mai segreti nel codice; solo dati sintetici nei test; dipendenze senza vulnerabilità critiche; nessuna spesa, invio a terzi, pubblicazione sugli store o modifica in produzione senza conferma di Gian.

## 4. Protocollo per le AI

1. **All'inizio di ogni sessione leggi, in ordine:** `LINEE_GUIDA.md` → `AGENTS.md` (comprese le deroghe) → `STATO.md` → i documenti che questi indicano. Poi fai il **giro di controllo** del capitolo 8.
2. **Firma tutto ciò che aggiungi:** `[Codex]` (ChatGPT/Codex), `[Claude]`, `[Gemini]`, `[Copilot]`, `[Gian]`, `[Altro: nome]`.
3. **`AGENTS.md` si aggiunge, non si riscrive.** Nuova sezione: `## [Firma] Titolo — AAAA-MM-GG`. Non cancellare né riformulare sezioni altrui. Per superarne una scrivi `## [Firma] Rettifica: <titolo> — AAAA-MM-GG`. Rispetta l'ordine già usato nel file.
4. La sezione `[Gian] Protocollo comune` in cima ad `AGENTS.md` e le righe `@LINEE_GUIDA.md` / `@AGENTS.md` dei file di ingresso non si toccano.
5. Se un documento contraddice il codice, **vale il codice**: scrivi la discrepanza e correggi il documento.
6. Comunica con Gian in italiano, in breve: cosa è fatto, cosa resta, cosa serve da lui. Le decisioni che spettano a lui si chiedono, non si indovinano.

## 5. `STATO.md`

Massimo una pagina, sezioni fisse: **Cos'è** · **Fase** (`idea`, `in sviluppo`, `test interno`, `beta pubblica`, `pubblicata`, `in pausa`, `archiviata`) · **Dove è pubblicata** (link verificabili) · **Prossimi passi** (max 5) · **Blocchi** (e chi deve sbloccarli) · **Componenti condivisi** (usati / offerti) · **Linee guida** (versione seguita) · **Registro aggiornamenti** (`AAAA-MM-GG [Firma] cosa è cambiato`, solo aggiunte).
Si aggiorna nella stessa PR del lavoro. Se cambia la fase si aggiorna anche `STATO_APP.md` nel registro.

## 6. Deroghe

- Solo Gian può concederle. Si scrivono nell'`AGENTS.md` del repository in una sezione `## [Gian] Deroghe alle linee guida`, una riga per deroga: cosa, perché, da quando.
- Un'AI che ritiene necessaria una deroga **la propone** a Gian (nella PR o in chat) e non la applica finché lui non la approva.
- Il controllo automatico considera conformi i punti coperti da deroga.

## 7. Aggiornamento delle linee guida

- Le modifiche si fanno solo nell'originale, nel registro, con una pull request che Gian approva. Si incrementa la versione: `1.0.1` correzioni di forma, `1.1.0` regole nuove, `2.0.0` cambi che richiedono interventi nei repository.
- Quando l'originale cambia su `main`, l'automazione del registro apre in ogni repository di `repository.txt` una pull request con la nuova copia e i file di ingresso aggiornati. Approvandola, il repository è allineato.
- Il controllo automatico di ogni repository segnala se la copia è più vecchia dell'originale.

## 8. Giro di controllo coordinato

Lo scopo è che nessuno rifaccia ciò che esiste già in un altro repository, e che il percorso di studio di Gian (Master Vibe) segua quello che sta davvero facendo.

### 8.1 All'inizio di ogni sessione (ogni AI: Codex, Claude, Gemini, Copilot…)
1. Leggi l'ultimo **diario** in `registro-delle-idee/diario/` (uno al giorno) e `MAPPA_COLLEGAMENTI.md`.
2. Prima di sviluppare qualcosa, chiediti: esiste già in un altro repository? Se sì, **riusalo** (cap. 3, regola 6) e cita l'origine.
3. Se non hai accesso al registro, scrivilo nella PR: il controllo resta da fare.

### 8.2 Ogni giorno (automatico)
Un giro di controllo programmato legge le novità di tutti i repository di `repository.txt` (commit, pull request, `STATO.md`) e scrive il diario del giorno nel registro:
- **cosa è cambiato** in ogni progetto;
- **sovrapposizioni**: lavori simili in repository diversi, con il suggerimento di quale codice riusare;
- **aggiornamenti** per `MAPPA_COLLEGAMENTI.md` e `STATO_APP.md`;
- **cosa serve da Gian**.

I file del diario e gli aggiornamenti automatici di mappa e stato si scrivono direttamente su `main` del registro, senza pull request: sono resoconti, non decisioni.

### 8.3 Ogni settimana
Il diario della domenica riassume la settimana: componenti da estrarre in una libreria comune, progetti fermi, duplicazioni da risolvere.

### 8.4 Collegamento con Master Vibe
Ogni giorno il giro aggiorna anche `Master-Vibe/02_WEEKLY_DIGEST/`: quali competenze sono state usate e quali argomenti del piano di studio diventano utili per il lavoro in corso. **Master Vibe è pubblico**: lì si scrivono solo argomenti e competenze, mai nomi di repository privati, codice proprietario o dati personali.

## 9. Registro delle versioni

- **1.1.0 — 2026-11-26 [Claude, su richiesta di Gian]** Capitolo 8: giro di controllo coordinato (all'avvio di ogni sessione, diario giornaliero automatico, riepilogo settimanale, collegamento con Master Vibe).
- **1.0.0 — 2026-11-26 [Claude, su richiesta di Gian]** Prima versione: flusso idea → progetto, struttura standard, regole di lavoro, protocollo per le AI, `STATO.md`, deroghe, aggiornamento centralizzato.
