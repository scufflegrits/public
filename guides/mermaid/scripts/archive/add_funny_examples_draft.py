"""Historical draft generator, retained for review rather than maintenance.

Its original logic is encapsulated below and never called automatically. The final
Markdown contains later edits; running this draft would not reproduce that final file.
Use the rendering/checking helpers to maintain the current documents instead.
"""


def original_draft():
    from pathlib import Path
    p=Path('funny.md')
    s=p.read_text().replace('Twelve fictional examples','Twenty-four fictional examples')
    examples=[
    ('Requirements telephone', 'Sequence messages reveal where an assumption enters a conversation. Responses make the mismatch visible before implementation.', '''%% Each handoff preserves confidence better than meaning.
    sequenceDiagram
      participant REQ_CUSTOMER as Customer
      participant REQ_ANALYST as Analyst
      participant REQ_ENGINEER as Engineer
      REQ_CUSTOMER->>REQ_ANALYST: I need a light application.
      REQ_ANALYST->>REQ_ENGINEER: It must be lightweight.
      REQ_ENGINEER-->>REQ_ANALYST: Removed every dependency.
      REQ_ANALYST-->>REQ_CUSTOMER: It is extremely lightweight.
      REQ_CUSTOMER->>REQ_ANALYST: Great. Where is the dark-mode toggle?
      Note over REQ_ANALYST: Schedule a requirements clarification.
    '''),
    ('Requirements freeze, now with a defrost cycle', 'Decision nodes distinguish approved changes from clarification. A loop shows why an approval process still needs an exit.', '''%% The freezer is working; someone keeps opening the door.
    flowchart TB
      FREEZE_BASELINE["Requirements approved"]
      FREEZE_REQUEST["One tiny clarification arrives"]
      FREEZE_CHANGE{"Does behavior change?"}
      FREEZE_REVIEW["Review scope, cost, and date"]
      FREEZE_APPROVED{"Change approved?"}
      FREEZE_UPDATE["Update the baseline"]
      FREEZE_BACKLOG["Backlog it for the sequel"]
      FREEZE_SHIP["Build the agreed version"]

      FREEZE_BASELINE --> FREEZE_REQUEST
      FREEZE_REQUEST --> FREEZE_CHANGE
      FREEZE_CHANGE -->|"No"| FREEZE_SHIP
      FREEZE_CHANGE -->|"Yes, but only completely"| FREEZE_REVIEW
      FREEZE_REVIEW --> FREEZE_APPROVED
      FREEZE_APPROVED -->|"Yes"| FREEZE_UPDATE
      FREEZE_APPROVED -->|"No"| FREEZE_BACKLOG
      FREEZE_UPDATE --> FREEZE_REQUEST
      FREEZE_BACKLOG --> FREEZE_SHIP
    '''),
    ('More engineers, faster onboarding meetings', 'Independent Gantt sections can compare hypothetical staffing scenarios with the same start date. Dependencies show when work must wait.', '''%% Invented durations illustrate coordination cost, not a staffing forecast.
    gantt
      title Two plans for the same tiny feature
      dateFormat YYYY-MM-DD
      axisFormat %b %d
      tickInterval 1day
      section One familiar engineer
        Implement and test :STAFF_SOLO, 2026-11-02, 5d
        Ship :milestone, STAFF_SOLO_SHIP, after STAFF_SOLO, 0d
      section Add eight new engineers
        Explain the repository :STAFF_ORIENT, 2026-11-02, 3d
        Agree on branch names :STAFF_BRANCH, after STAFF_ORIENT, 2d
        Implement and resolve conflicts :STAFF_BUILD, after STAFF_BRANCH, 5d
        Ship with a larger group photo :milestone, STAFF_GROUP_SHIP, after STAFF_BUILD, 0d
    '''),
    ('Parallel requests, serial human', 'A sequence diagram can show concurrent requests with `par` and `and`. Concurrent arrivals do not imply that one engineer can execute them simultaneously.', '''%% Three channels discover the same available engineer.
    sequenceDiagram
      participant FOCUS_PM as Project manager
      participant FOCUS_ENGINEER as Engineer
      participant FOCUS_OPS as Operations
      participant FOCUS_CHAT as Team chat
      par Project request
        FOCUS_PM->>FOCUS_ENGINEER: Can you focus on the feature?
      and Incident request
        FOCUS_OPS->>FOCUS_ENGINEER: Can you focus on this alert?
      and Collaboration request
        FOCUS_CHAT->>FOCUS_ENGINEER: Can you join a focus meeting?
      end
      FOCUS_ENGINEER->>FOCUS_ENGINEER: Reload mental context
      Note over FOCUS_ENGINEER: CPU count remains one human.
      FOCUS_ENGINEER-->>FOCUS_PM: Which focus is the priority?
    '''),
    ('Traceability to the one laptop', 'A requirement diagram links a requirement to its implementation and verification evidence. The deliberately narrow requirement exposes the portability gap.', '''%% A passing demonstration proves only the requirement that was written.
    requirementDiagram
      requirement REQ_LAPTOP {
        id: R1
        text: "Application shall start on the demo laptop."
        risk: high
        verifymethod: demonstration
      }
      element REQ_BUILD {
        type: application
        docref: "demo-build.md"
      }
      element REQ_DEMO {
        type: demonstration
        docref: "works-on-my-machine.md"
      }

      REQ_BUILD - satisfies -> REQ_LAPTOP
      REQ_DEMO - verifies -> REQ_LAPTOP
    '''),
    ('The temporary workaround retirement plan', 'State transitions can include a return to an earlier state. The final state makes the actual retirement condition explicit.', '''%% Temporary is a lifecycle stage with a surprisingly long lease.
    stateDiagram-v2
      state "Temporary workaround" as WORKAROUND_TEMP
      state "Used by every team" as WORKAROUND_SHARED
      state "Business-critical infrastructure" as WORKAROUND_CRITICAL
      state "Replacement proposed" as WORKAROUND_REPLACE
      state "Retired and documented" as WORKAROUND_RETIRED

      [*] --> WORKAROUND_TEMP
      WORKAROUND_TEMP --> WORKAROUND_SHARED: Someone shares the script
      WORKAROUND_SHARED --> WORKAROUND_CRITICAL: Nobody knows its owner
      WORKAROUND_CRITICAL --> WORKAROUND_REPLACE: Annual cleanup initiative
      WORKAROUND_REPLACE --> WORKAROUND_CRITICAL: Budget moves to next year
      WORKAROUND_REPLACE --> WORKAROUND_RETIRED: Replacement works and users migrate
      WORKAROUND_RETIRED --> [*]
    '''),
    ('A factory for manufacturing factories', 'A class dependency arrow means one class uses another. A creation dependency does not claim inheritance or ownership.', '''%% Abstraction has become the primary manufactured product.
    classDiagram
      class BUILD_FACTORY_FACTORY["FactoryFactory"] {
        +createFactory()
      }
      class BUILD_FACTORY["Factory"] {
        +createWidget()
      }
      class BUILD_WIDGET["Widget"] {
        +doTheActualThing()
      }
      class BUILD_REVIEW["ArchitectureReview"] {
        +requestAnotherLayer()
      }

      BUILD_FACTORY_FACTORY ..> BUILD_FACTORY : creates
      BUILD_FACTORY ..> BUILD_WIDGET : creates
      BUILD_REVIEW ..> BUILD_FACTORY_FACTORY : requests
    '''),
    ('The staffing spreadsheet discovered cloning', 'An associative entity models a many-to-many relationship. Cardinality does not enforce a sum across rows: capacity needs a separate business rule.', '''%% Three allocations of 50 percent do not create half an extra engineer.
    erDiagram
      STAFF_ENGINEER {
        int engineer_id PK
        string name
        int actual_capacity_percent "100, despite the spreadsheet"
      }
      STAFF_PROJECT {
        int project_id PK
        string name
        string priority "Always highest"
      }
      STAFF_ALLOCATION {
        int allocation_id PK
        int engineer_id FK
        int project_id FK
        int assigned_percent "50 per project, apparently harmless"
      }

      STAFF_ENGINEER ||--o{ STAFF_ALLOCATION : stretches_into
      STAFF_PROJECT ||--o{ STAFF_ALLOCATION : requests
    '''),
    ('The universal standard recruitment drive', 'A timeline orders labeled periods and their events. Unlike a Gantt chart, it does not calculate duration or dependencies.', '''%% The committee succeeds at increasing the number of standards.
    timeline
      title One standard to unite them all
      Week 1 : Discover fourteen competing standards
      Week 2 : Form a committee to simplify things
      Week 3 : Publish the universal replacement
      Week 4 : Support fifteen competing standards
    '''),
    ('Automating a five-second task', 'A feedback loop can model repeated investment. A decision gives the loop an exit rather than implying that improvement must continue forever.', '''%% The calculator is the only component with a positive return so far.
    flowchart TB
      AUTO_TASK["Manual task takes five seconds"]
      AUTO_SCRIPT["Spend a day automating it"]
      AUTO_DEPENDENCY["Add configuration and dependencies"]
      AUTO_BROKEN["Automation needs maintenance"]
      AUTO_CALCULATE["Calculate the break-even date"]
      AUTO_WORTH{"Will we run it that often?"}
      AUTO_KEEP["Keep it simple and document it"]

      AUTO_TASK --> AUTO_SCRIPT
      AUTO_SCRIPT --> AUTO_DEPENDENCY
      AUTO_DEPENDENCY --> AUTO_BROKEN
      AUTO_BROKEN --> AUTO_CALCULATE
      AUTO_CALCULATE --> AUTO_WORTH
      AUTO_WORTH -->|"Yes, fix it"| AUTO_SCRIPT
      AUTO_WORTH -->|"No, not before retirement"| AUTO_KEEP
    '''),
    ('High availability, except during Pat\'s vacation', 'Named edges allow styling by meaning. A dotted arrow shows a knowledge dependency; it does not represent a redundant network link.', '''%% Three replicas still depend on one person's memory.
    flowchart TB
      subgraph SG_VACATION_PLATFORM["Highly available platform"]
        VACATION_SERVICE_01["Service replica 1"]
        VACATION_SERVICE_02["Service replica 2"]
        VACATION_SERVICE_03["Service replica 3"]
      end
      VACATION_PAT["Pat: remembers the recovery command"]
      VACATION_RUNBOOK["Runbook: ask Pat"]

      VACATION_SERVICE_01 edge_replica_01_pat_knowledge@-.->|"Recovery knowledge"| VACATION_PAT
      VACATION_SERVICE_02 edge_replica_02_pat_knowledge@-.->|"Recovery knowledge"| VACATION_PAT
      VACATION_SERVICE_03 edge_replica_03_pat_knowledge@-.->|"Recovery knowledge"| VACATION_PAT
      VACATION_RUNBOOK edge_runbook_pat_knowledge@-.->|"Escalation procedure"| VACATION_PAT

      classDef groupPlatform fill:#111827,stroke:#94a3b8,color:#f1f5f9
      classDef edgeKnowledge stroke:#fbbf24,stroke-width:2px,stroke-dasharray:3 3
      class SG_VACATION_PLATFORM groupPlatform
      class edge_replica_01_pat_knowledge,edge_replica_02_pat_knowledge,edge_replica_03_pat_knowledge edgeKnowledge
      class edge_runbook_pat_knowledge edgeKnowledge
    ''')]
    for i,(title,note,body) in enumerate(examples,13):
        layout='  # Keep flowchart groups and branches predictable where supported.\n  layout: elk\n' if '\nflowchart ' in body else ''
        s+=f'\n## {i}. {title}\n\n**Teaching point:** {note}\n\n```mermaid\n---\nconfig:\n  # Keep this example consistent with the dark presentation.\n  theme: dark\n{layout}  # Match the image export canvas.\n  themeVariables:\n    background: "#0b1120"\n---\n{body}```\n'
        if i==17:
            s+='\nPassing this demonstration says nothing about other laptops. Add portability\nrequirements and their own verification evidence when portability matters.\n'
        if i==20:
            s+='\nFor example, assigning one engineer to three projects at 50% each totals 150%.\nThe database needs a capacity check; a crow\'s-foot connector cannot enforce it.\n'
        if i==23:
            s+='\n**Legend:** dotted amber arrows show dependence on recovery knowledge.\nThe platform boundary groups services; it does not imply independent operators.\n'
    p.write_text(s)


if __name__ == '__main__':
    raise SystemExit('Archived draft only; no files written. See scripts/README.md.')
