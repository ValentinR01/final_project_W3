<script>
  import Margin from "../../../../components/atoms/Margin.svelte";
import Pagination from "../../../../components/atoms/Pagination.svelte";
  import Text from "../../../../components/atoms/Text.svelte";
  import Searchbar from "../../../../components/molecules/Searchbar.svelte";
  import EmployeeCard from "../../../../components/molecules/cards/EmployeeCard.svelte";

  export let data;

  /**
   * @type {any}
   */
  let values;

</script>

<Margin marginTop='3%'>
  <div class='card block-center'>
    <Margin marginBottom='35px'>
      <Text
        textTag='h1'
        class='text-preset-1 text-center text--uppercase'
      >
        EQUIPE
      </Text>
    </Margin>
  
    <Searchbar urlSearchbar="users" class='block-center' data={data.users} widthSearchbar="380" />
  
    <Margin marginBottom='20px' marginTop='20px'>
      {#if values}
        <div class='employee-cards'>
          {#each values as value}
            <EmployeeCard employeePicture={value.profile_pic}>
              <span slot='name'>{value.fullname}</span>
              <span slot='number-projects'>{value.count_assigning_asset}</span>
            </EmployeeCard>
          {/each}
        </div>
      {/if}
    </Margin>
  
    <Pagination rows={data.users} perPage={6} bind:trimmedRows={values} />
  </div>  
</Margin>

<style>
  .employee-cards{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    row-gap: var(--spacing-2);
  }
</style>