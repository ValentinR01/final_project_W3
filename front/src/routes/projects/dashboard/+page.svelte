<script lang="ts">
  import Text from '../../../components/atoms/Text.svelte';
  import Tabs from '../../../components/molecules/Tabs.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';

  import RegularOngoing from '../../../tabs/Regular Dashboard/RegularOngoing.svelte';
  import RegularToStart from '../../../tabs/Regular Dashboard/RegularToStart.svelte';
  import Link from '../../../components/atoms/Link.svelte';
  import Searchbar from "../../../components/molecules/Searchbar.svelte";
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import TableProjects from '../../../components/organisms/TableProjects.svelte';

  let domain = 'regisseur';
  export let data;

  let items = [
    { label: "A commencer",
     value: 1,
     component: RegularToStart
    },
    { label: "En cours",
     value: 2,
     component: RegularOngoing
    }
  ];

  let rowElements : any = data.asset;

  let selectedRowElements = rowElements.map((
    { title, has_high_priority, categorie }: any) => ({ title, has_high_priority, categorie }
  ));
  let selectedValues = selectedRowElements;

</script>
{#if domain == 'regisseur'}
  <Link linkUrl='/projects/create' linkColor='white' class='link--button'> + Nouveau projet </Link>
  <div class="container--global">
    <div class="block--left">
      <Margin marginTop='3%'>
        <div class='card card--left block-center'>
          <div class="container--head">
            <Text
            textTag='h1'
            class='text-preset-1 text--uppercase'
            >
            Projets créés
            </Text>
            <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
          </div>

          <div class="table-container">
            <Margin marginTop='40px'>
              <TableProjects {selectedRowElements} />
            </Margin>
          
            <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
          </div>
        </div>
      </Margin>
    </div>
    <div class="block--right">
      <Margin marginTop='3%'>
        <div class='card card--right block-center'>
          <div class="container--head">
            <Text
            textTag='h1'
            class='text-preset-1 text--uppercase'
            >
            Projets captés
            </Text>
            <Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="190" />
          </div>

          <div class="table-container">
            <Margin marginTop='40px'>
              <TableProjects {selectedRowElements} />
            </Margin>
          
            <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
          </div>
          
        </div>
      </Margin>
    </div>
  </div>
  
{:else}
  <Margin marginTop='3%'>
    <div class='card block-center'>
      <Text
        textTag='h1'
        class='text-preset-1 text-center text--uppercase'
        >
        Les projets
      </Text>

      <div class='dashboard-nav'>
        <Tabs {items} data={data}/>
      </div>
    </div>
  </Margin>
{/if}


<style>
  .dashboard-nav{
    position: relative;
    margin-top: var(--spacing-5);
  }
  .container--global {
    width:auto;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .card--left,
  .card--right {
    width: 80%;
  }
  .block--left,
  .block--right {
    display: inline-block;
    vertical-align: top;
  }
  .block--left {
    width:45%;
    margin-right: var(--spacing-2);
  }
  .block--right {
    width:45%;
    margin-left: var(--spacing-2);
  }
  .container--head {
    display: flex;
    justify-content: space-between;
  }

</style>