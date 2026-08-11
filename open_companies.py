"""
Opens each company website in your default web browser, 5 at a time.
Remembers how many you've opened so far (in progress.json, next to this
script) so re-running it picks up right where you left off. You can pause
between batches, and resume any time by just running the script again.

Usage:
    python open_companies.py            # resume from last position
    python open_companies.py --reset    # start over from the beginning
"""

import json
import sys
import webbrowser
import time
from pathlib import Path

PROGRESS_FILE = Path(__file__).with_name("progress.json")
BATCH_SIZE = 5

websites = [
    "https://together.ai",
    "https://fireworks.ai",
    "https://baseten.co",
    "https://modal.com",
    "https://replicate.com",
    "https://anyscale.com",
    "https://wandb.ai",
    "https://hex.tech",
    "https://retool.com",
    "https://airbyte.com",
    "https://fivetran.com",
    "https://getcensus.com",
    "https://hightouch.com",
    "https://getdbt.com",
    "https://montecarlodata.com",
    "https://metaplane.dev",
    "https://bigeye.com",
    "https://sigmacomputing.com",
    "https://preset.io",
    "https://mode.com",
    "https://thoughtspot.com",
    "https://alteryx.com",
    "https://dominodatalab.com",
    "https://pachyderm.com",
    "https://determined.ai",
    "https://grid.ai",
    "https://comet.com",
    "https://neptune.ai",
    "https://clear.ml",
    "https://iguazio.com",
    "https://tecton.ai",
    "https://featureform.com",
    "https://hopsworks.ai",
    "https://vespa.ai",
    "https://pinecone.io",
    "https://weaviate.io",
    "https://qdrant.tech",
    "https://trychroma.com",
    "https://langchain.com",
    "https://llamaindex.ai",
    "https://vellum.ai",
    "https://humanloop.com",
    "https://braintrust.dev",
    "https://arize.com",
    "https://whylabs.ai",
    "https://rungalileo.io",
    "https://fiddler.ai",
    "https://robustintelligence.com",
    "https://hiddenlayer.com",
    "https://protectai.com",
    "https://lakera.ai",
    "https://cranium.ai",
    "https://calypsoai.com",
    "https://credo.ai",
    "https://runwayml.com",
    "https://pika.art",
    "https://lumalabs.ai",
    "https://synthesia.io",
    "https://elevenlabs.io",
    "https://suno.com",
    "https://assemblyai.com",
    "https://deepgram.com",
    "https://speechmatics.com",
    "https://gladia.io",
    "https://poly.ai",
    "https://sierra.ai",
    "https://decagon.ai",
    "https://cresta.com",
    "https://observe.ai",
    "https://ada.cx",
    "https://forethought.ai",
    "https://ironcladapp.com",
    "https://harvey.ai",
    "https://casetext.com",
    "https://hebbia.ai",
    "https://glean.com",
    "https://writer.com",
    "https://jasper.ai",
    "https://copy.ai",
    "https://contentsquare.com",
    "https://amplitude.com",
    "https://heap.io",
    "https://pendo.io",
    "https://fullstory.com",
    "https://logrocket.com",
    "https://datadoghq.com",
    "https://honeycomb.io",
    "https://chronosphere.io",
    "https://grafana.com",
    "https://newrelic.com",
    "https://sysdig.com",
    "https://lacework.com",
    "https://wiz.io",
    "https://orca.security",
    "https://snyk.io",
    "https://semgrep.dev",
    "https://socket.dev",
    "https://chainguard.dev",
    "https://vanta.com",
    "https://drata.com",
    "https://secureframe.com",
    "https://onetrust.com",
    "https://bigid.com",
    "https://cyera.io",
    "https://island.io",
    "https://netskope.com",
    "https://zscaler.com",
    "https://cloudflare.com",
    "https://fastly.com",
    "https://vercel.com",
    "https://netlify.com",
    "https://render.com",
    "https://railway.app",
    "https://fly.io",
    "https://northflank.com",
    "https://porter.run",
    "https://cortex.io",
    "https://harness.io",
    "https://circleci.com",
    "https://buildkite.com",
    "https://semaphoreci.com",
    "https://nx.dev",
    "https://turbo.build",
    "https://planetscale.com",
    "https://neon.tech",
    "https://supabase.com",
    "https://cockroachlabs.com",
    "https://timescale.com",
    "https://singlestore.com",
    "https://clickhouse.com",
    "https://materialize.com",
    "https://risingwave.com",
    "https://redpanda.com",
    "https://streamnative.io",
    "https://ververica.com",
    "https://decodable.co",
    "https://estuary.dev",
    "https://meroxa.com",
    "https://rilldata.com",
    "https://cube.dev",
    "https://metabase.com",
    "https://omni.co",
    "https://y42.com",
    "https://ascend.io",
    "https://prefect.io",
    "https://dagster.io",
    "https://astronomer.io",
    "https://temporal.io",
    "https://windmill.dev",
    "https://trigger.dev",
    "https://inngest.com",
    "https://zeet.co",
    "https://qovery.com",
    "https://doppler.com",
    "https://infisical.com",
    "https://hashicorp.com",
    "https://pulumi.com",
    "https://env0.com",
    "https://spacelift.io",
    "https://firefly.ai",
    "https://opslevel.com",
    "https://backstage.io",
    "https://getport.io",
    "https://gitpod.io",
    "https://codesandbox.io",
    "https://stackblitz.com",
    "https://replit.com",
    "https://cursor.com",
    "https://magic.dev",
    "https://poolside.ai",
    "https://codeium.com",
    "https://tabnine.com",
    "https://sourcegraph.com",
    "https://snorkel.ai",
    "https://labelbox.com",
    "https://scale.com",
    "https://surgehq.ai",
    "https://invisible.co",
    "https://turing.com",
    "https://toloka.ai",
    "https://appen.com",
    "https://v7labs.com",
    "https://encord.com",
    "https://roboflow.com",
    "https://voxel51.com",
    "https://clarifai.com",
    "https://landing.ai",
    "https://covariant.ai",
    "https://physicalintelligence.company",
    "https://skild.ai",
    "https://figure.ai",
    "https://1x.tech",
    "https://apptronik.com",
    "https://chefrobotics.ai",
    "https://brightmachines.com",
    "https://path-robotics.com",
    "https://diligentrobots.com",
]

DELAY_SECONDS = 1.0  # pause between tabs within a batch


def load_progress() -> int:
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text()).get("done", 0)
        except (json.JSONDecodeError, OSError):
            return 0
    return 0


def save_progress(done: int) -> None:
    PROGRESS_FILE.write_text(json.dumps({"done": done}))


def main():
    if "--reset" in sys.argv:
        save_progress(0)
        print("Progress reset to 0.")

    done = load_progress()
    total = len(websites)

    if done >= total:
        print(f"All {total} websites already opened. Run with --reset to start over.")
        return

    print(f"Resuming at company {done + 1} of {total}.")

    while done < total:
        batch = websites[done : done + BATCH_SIZE]
        print(f"\nOpening companies {done + 1}-{done + len(batch)} of {total}:")
        for i, url in enumerate(batch, start=done + 1):
            print(f"  [{i}/{total}] {url}")
            webbrowser.open_new_tab(url)
            time.sleep(DELAY_SECONDS)

        done += len(batch)
        save_progress(done)  # saved after every batch, so a crash won't lose progress

        if done >= total:
            print("\nDone! All websites have been opened.")
            break

        answer = input(f"\nOpened {done}/{total} so far. Press Enter for next 5, or type 'q' to pause: ").strip().lower()
        if answer == "q":
            print(f"Paused at {done}/{total}. Run the script again to resume from here.")
            break


if __name__ == "__main__":
    main()
