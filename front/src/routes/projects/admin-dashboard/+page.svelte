<script lang="ts">
  import Text from '../../../components/atoms/Text.svelte';
  import Tabs from '../../../components/molecules/Tabs.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';
  import Searchbar from "../../../components/molecules/Searchbar.svelte";
  import Pagination from '../../../components/atoms/Pagination.svelte';

  import SuperadminVideo from "../../../tabs/SuperAdmin Dashboard/SuperadminVideo.svelte";
  import SuperadminFinal from "../../../tabs/SuperAdmin Dashboard/SuperadminFinal.svelte";
  import SuperadminOngoing from "../../../tabs/SuperAdmin Dashboard/SuperadminOngoing.svelte";

  import AdminAttribution from '../../../tabs/Admin Dashboard/AdminAttribution.svelte';
  import AdminOngoing from '../../../tabs/Admin Dashboard/AdminOngoing.svelte';
  import AdminToCome from '../../../tabs/Admin Dashboard/AdminToCome.svelte';

  import TableProjects from '../../../components/organisms/TableProjects.svelte';
  import { user } from "../../../store";

  export let data;

  let rowElements : any = data.asset;

  let selectedRowElements: Array<any>;
  let selectedValues: Array<any>;

  selectedRowElements = rowElements.map((
    { title, has_high_priority, categorie, created_at }: any) => ({ title, has_high_priority, categorie, created_at}
  ));
  selectedValues = selectedRowElements

  let role = 'admin';
  let domain = 'regisseur';

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
  
    <div class='dashboard-nav'>
      {#if role == 'superadmin'}
        <Text
          textTag='h1'
          class='text-preset-1 text-center text--uppercase'
          >
          Les projets
        </Text>
        <Margin marginTop='40px'>
          <Tabs items={itemsSuperAdmin} data={data}/>
        </Margin>
      {:else if role == 'admin'}
        {#if domain == 'regisseur'}
        <Text
          textTag='h1'
          class='text-preset-1 text-center text--uppercase'
          >
          Projets en captation
        </Text>
          <div class="table-container">
            <Margin marginTop='40px'>
              <TableProjects {selectedRowElements} />
            </Margin>
          
            <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
            <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
          </div>
        {:else}

        <Text
          textTag='h1'
          class='text-preset-1 text-center text--uppercase'
          >
          Les projets
        </Text>
        <Margin marginTop='40px'>
          <Tabs items={itemsAdmin} data={data}/>
        </Margin>
        
        {/if}
      {/if }
    </div>
  
  </div>
</Margin>

<style>
  .dashboard-nav{
    position: relative;
  }
  :global(.searchbar-container) {
    top: 66px!important;
  }
</style>