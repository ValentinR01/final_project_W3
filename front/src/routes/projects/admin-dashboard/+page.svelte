<script>
  import Text from '../../../components/atoms/Text.svelte';
  import Tabs from '../../../components/molecules/Tabs.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';

  import SuperadminVideo from "../../../tabs/SuperAdmin Dashboard/SuperadminVideo.svelte";
  import SuperadminFinal from "../../../tabs/SuperAdmin Dashboard/SuperadminFinal.svelte";
  import SuperadminOngoing from "../../../tabs/SuperAdmin Dashboard/SuperadminOngoing.svelte";

  import AdminAttribution from '../../../tabs/Admin Dashboard/AdminAttribution.svelte';
  import AdminOngoing from '../../../tabs/Admin Dashboard/AdminOngoing.svelte';
  import AdminToCome from '../../../tabs/Admin Dashboard/AdminToCome.svelte';

  export let data;
  const { projects } = data;

  let role = 'admin';

  let itemsSuperAdmin = [
    { label: "Validation montage",
     value: 1,
     component: SuperadminVideo
    },
    { label: "Validation finale",
     value: 2,
     component: SuperadminFinal
    },
    { label: "En cours",
     value: 3,
     component: SuperadminOngoing
    }
  ];

  let itemsAdmin = [
    { label: "A attribuer",
     value: 1,
     component: AdminAttribution
    },
    { label: "En cours",
     value: 2,
     component: AdminOngoing
    },
    { label: "A venir",
     value: 3,
     component: AdminToCome
    }
  ];
</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <Text
      textTag='h1'
      class='text-preset-1 text-center text--uppercase'
      >
      Les projets
    </Text>
  
    <br><br>
    <p class="text-preset-Z text-center">AJOUTER TABLEAUX</p>

    {#if projects}
      <div class='dashboard-nav'>
        {#if role == 'superadmin'}
          <Tabs items={itemsSuperAdmin} data={projects}/>
        {:else if role == 'admin'}
          <Tabs items={itemsAdmin} data={projects}/>
        {/if }
      </div>
  
      <p> TEST DE DATA A SUPPRIMER LORS DE L'AJOUT DES TABLEAUX </p>
      {#each projects as project}
        {project.title}
        {project.created_at}
        {project.has_high_priority}
        {project.step_lifecycle_id}
      {/each}
    {:else}
      <Margin marginTop='var(--spacing-5)' marginBottom='var(--spacing-6)'>
        <Text textTag='p'class='text-preset-4 text-center'>
          Vous n'avez pas encore de projets.
        </Text>
      </Margin>
    {/if}
  </div>
</Margin>

<style>
  .dashboard-nav{
    position: relative;
    margin-top: var(--spacing-5);
  }
</style>