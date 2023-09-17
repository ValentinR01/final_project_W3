<script lang="ts">
  import Link from '../../../components/atoms/Link.svelte';
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';
  import Searchbar from '../../../components/molecules/Searchbar.svelte';
  import TableUsers from '../../../components/organisms/TableUsers.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';
  import Icon from '../../../components/atoms/Icon.svelte';
  import Image from '../../../components/atoms/Image.svelte';

  import { user } from '../../../store';

  export let data;

  let rowElements : any = data.users;

	let selectedRowElements = rowElements.map((
    { profile_pic, fullname, email, domain, role, id }: any) => ({ profile_pic, fullname, email, domain, role, id }
  ));

  let selectedValues = selectedRowElements
</script>

{#if $user.role == 'superadmin'}
  <div class='card block-center'>
    <Text
      textTag='h1'
      class='text-preset-1 text-center text--uppercase'
      >
      Les utilisateurs
    </Text>
  
    <div class="table-container">
      <Margin marginTop='var(--spacing-3)' marginBottom="var(--spacing-3)">
        <div class='dashboard-nav'>
          <Searchbar urlSearchbar="projects" data={data.users} widthSearchbar="190" />
          <Link linkUrl='/users/create' linkColor='white' class='link--button'> Ajouter </Link>
        </div>
      </Margin>
  
      <Margin marginTop="var(--spacing-3)">
        <TableUsers {selectedRowElements} />
      </Margin>
    </div>
  
    <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
  </div>
{:else}
  <div class='card block-center'>
    <Text
      textTag='p'
      class='text-preset-4 text-center'
    >
      Vous n'avez pas accès à cette page.
    </Text>

    <Margin marginTop='var(--spacing-3)'>
      {#if $user.role == 'lead'}
        <Link linkUrl='/projects/admin-dashboard' linkColor='white' class='link--button link-center'> Retour </Link>
      {:else}
        <Link linkUrl='/projects/dahboard' linkColor='white' class='link--button link-center'> Retour </Link>
      {/if}
    </Margin>
  </div>
{/if}

<style>
  .table-container {
    display: table;
    margin-right: auto;
    margin-left: auto;
  }

  .dashboard-nav{
    display: flex;
    justify-content: space-between;
    margin-top: var(--spacing-5);
  }
</style>