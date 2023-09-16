<script lang="ts">

  import UserIcon from '../../../assets/icons/UserIcon.svelte';
  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';
  import Searchbar from '../../../components/molecules/Searchbar.svelte';
  import Button from '../../../components/atoms/Button.svelte';
  import TableUsers from '../../../components/organisms/TableUsers.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';
  import Icon from '../../../components/atoms/Icon.svelte';
  import Image from '../../../components/atoms/Image.svelte';
  import ArrowBackgroundIcon from '../../../assets/icons/ArrowBackgroundIcon.svelte';

  export let data;

  let rowElements : any = data.users;

	let selectedRowElements = rowElements.map((
    { profile_pic, fullname, email, domain, role }: any) => ({ profile_pic, fullname, email, domain, role }
  ));

  let selectedValues = selectedRowElements
</script>

<div class='card block-center'>
  <Text
    textTag='h1'
    class='text-preset-1 text-center text--uppercase'
    >
    Les utilisateurs
  </Text>

  <div class="table-container">
    <Margin marginTop='15px'>
      <div class='dashboard-nav'>
        <Searchbar urlSearchbar="projects" data={data.users} widthSearchbar="190" />
        <Button> Ajouter </Button>
      </div>
    </Margin>

    <Margin marginTop="var(--spacing-3)">
      <TableUsers {selectedRowElements} />
    </Margin>
  </div>

  <Pagination rows={selectedValues} perPage={3} bind:trimmedRows={selectedRowElements} />
</div>

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

  .data-exemple{
    display: flex;
    column-gap: 20px;
    row-gap: 20px;
    align-items: center;
  }
</style>