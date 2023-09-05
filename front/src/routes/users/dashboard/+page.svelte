<script>
  import UserIcon from '../../../assets/icons/UserIcon.svelte';

  import Pagination from '../../../components/atoms/Pagination.svelte';
  import Text from '../../../components/atoms/Text.svelte';
  import Searchbar from '../../../components/molecules/Searchbar.svelte';
  import Button from '../../../components/atoms/Button.svelte';
  import Link from '../../../components/atoms/Link.svelte';
  import Margin from '../../../components/atoms/Margin.svelte';
  import Icon from '../../../components/atoms/Icon.svelte';
  import Image from '../../../components/atoms/Image.svelte';
  import ArrowBackgroundIcon from '../../../assets/icons/ArrowBackgroundIcon.svelte';

  export let data;
  const { users } = data;

  /**
   * @type {any}
   */
  let values;

</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <Text
      textTag='h1'
      class='text-preset-1 text-center text--uppercase'
      >
      Les utilisateurs
    </Text>

    <div class='dashboard-nav'>
      <Searchbar urlSearchbar="projects" data={data.users} widthSearchbar="190" />
      <Link linkUrl='/users/create' linkColor='white' class='link--button'> Ajouter </Link>
    </div>

    <p class='text-center'> A REMPLACER PAR DASHBOARD USERS </p>

    <Margin marginTop="var(--spacing-3)">
      {#each users as user}
        <div class="data-exemple">
          {#if user.profile_picture != null }
          <Image
            imageSrc={user.profile.picture}
            imageAlt="User profile pic"
            imageWidth=50
          />
          {:else}
            <Icon name="user" width="50" height="50"> <UserIcon /> </Icon>
          {/if}
          <p>
            {user.name}
          </p>
          <p>
            {user.email}
          </p>
          <p>
            {user.domain_id}
          </p>
          <p>
            {user.role_id}
          </p>
          <Link
            linkUrl='/{user.id}'> 
            <Icon name="details" width="20" height="20"> <ArrowBackgroundIcon /> </Icon>
          </Link>
        </div>
      {/each}
    </Margin>
  
    <Pagination rows={data.users} perPage={5} bind:trimmedRows={values} />

  </div>
</Margin>

<style>
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